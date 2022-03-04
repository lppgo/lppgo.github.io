---
title: "01-docker registry http api v2"
author: "lucas" # 文章作者
description: "docker registry http api v2" # 文章描述信息
date: 2021-07-28
lastmod: 2021-07-28

tags: # 文章所属标签
  ["registry", "docker"]
categories: # 文章所属目录
  ["Docker"]
keywords: # 文章关键词
  ["registryAPI", "docker"]
---

<div align='center' ><font size='50'>docker registry http api v2</font></div>

<!-- [toc] -->

# Table of Contents

- [Table of Contents](#table-of-contents)
- [1: Overview](#1-overview)
- [2: 专有名词解释](#2-专有名词解释)
- [3: Push image 过程](#3-push-image-过程)
  - [3.1 Pushing a Layer（上传层）](#31-pushing-a-layer上传层)
    - [3.1.1 Existing Layers(检查层是否存在)](#311-existing-layers检查层是否存在)
    - [3.1.2 Starting An Upload(启动上传服务)](#312-starting-an-upload启动上传服务)
    - [3.1.3 Uploading the Layer(上传层)](#313-uploading-the-layer上传层)
      - [3.1.3.1 Upload Progress(上传进度)](#3131-upload-progress上传进度)
      - [3.1.3.2 Monolithic Upload(整块上传）](#3132-monolithic-upload整块上传)
      - [3.1.3.3 Chunked Upload（分块上传）](#3133-chunked-upload分块上传)
      - [3.1.3.4 Completed Upload(上传完成)](#3134-completed-upload上传完成)
      - [3.1.3.5 Canceling an Upload(取消上传)](#3135-canceling-an-upload取消上传)
      - [3.1.3.6 Cross Repository Blob Mount（交叉挂载层）](#3136-cross-repository-blob-mount交叉挂载层)
  - [3.2 Deleting a Layer(删除层)](#32-deleting-a-layer删除层)
  - [3.3 Pushing an Image Manifest（上传镜像清单）](#33-pushing-an-image-manifest上传镜像清单)
- [4: Pull image 过程](#4-pull-image-过程)
  - [4.1 Pulling an Image Manifest（拉取镜像清单）](#41-pulling-an-image-manifest拉取镜像清单)
  - [4.2 Pulling a Layer（拉取层）](#42-pulling-a-layer拉取层)
- [5: Retrieve 检索功能](#5-retrieve-检索功能)
  - [5.1 Listing Repositories（列出存储库）](#51-listing-repositories列出存储库)
  - [5.2 Pagination(部分列出存储库)](#52-pagination部分列出存储库)
  - [5.3 Listing Image Tags(列出镜像 tag)](#53-listing-image-tags列出镜像-tag)
  - [5.4 Pagination(部分列出镜像 tag)](#54-pagination部分列出镜像-tag)
- [6: Deleteing an Image（删除镜像）](#6-deleteing-an-image删除镜像)
- [7: Errors 错误信息](#7-errors-错误信息)

# 1: Overview

| methods | path                             | Entity                          | Description                                                                                                                                           |
| ------- | -------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET     | /v2/                             | Base                            | 检查 the endpoint 是否实现了 Docker Registry API V2.                                                                                                  |
| GET     | /v2/{name}/tags/list             | Tags                            | 通过 name 获取 repository 下的 tags                                                                                                                   |
| GET     | /v2/{name}/manifests/{reference} | Manifest                        | 获取由 name 和 references 标识的 manifest，其中 referencec 可以是 tag 或 digest。还可以向该 endpoint 发出 HEAD 请求以获取资源信息，而不接收所有数据。 |
| PUT     | /v2/{name}/manifests/{reference} | Manifest                        | Put 由 name 和 reference 标识的 manifest                                                                                                              |
| DELETE  | /v2/{name}/manifests/{reference} | Manifest                        | 删除由 digest 标识的 manifest                                                                                                                         |
| GET     | /v2/{name}/blobs/{digest}        | Blob                            | 从 registry retrieve 由 digest 标识的 blobs                                                                                                           |
| DELETE  | /v2/{name}/blobs/{digest}        | Blob                            | Delete the blob identified by name and digest                                                                                                         |
| POST    | /v2/{name}/blobs/uploads/        | Initiate(启动) Blob upload 服务 | 启动可恢复的 blob upload 服务。如果成功，将提供上载位置以完成上载。或者，如果存在 digest 参数，则请求正文将用于在单个请求中完成上载。                 |
| GET     | /v2/{name}/blobs/uploads/{uuid}  | Blob Upload                     | 检索由 uuid 标识的上传状态。此 endpoint 的主要目的是 resolve 可恢复 upload 的当前状态。                                                               |
| PATCH   | /v2/{name}/blobs/uploads/{uuid}  | Blob Upload                     | 上传 指定 upload 的 chunk 数据块                                                                                                                      |
| PUT     | /v2/{name}/blobs/uploads/{uuid}  | Blob Upload                     | 完成 uuid 指定的上传，可以选择附加 body 作为最后一个块                                                                                                |
| DELETE  | /v2/{name}/blobs/uploads/{uuid}  | Blob Upload                     | Cancel **outstanding** upload processes, releasing associated resources. If this is not called, the unfinished uploads will **eventually** timeout.   |
| GET     | /v2/\_catalog                    | Catalog                         | 在 registry 中检索一个有序的，可用的 repositry 的 json 列表                                                                                           |

# 2: 专有名词解释

- **repositry name**(存储库名称):存储库指在库中存储的镜像
- **digest**(摘要):是 image 各个层的唯一标识。虽然算法允许使用任意算法，但是为了兼容性应该使用 sha256。
  例：`sha256:6c3c624b58dbbcd3c0dd82b4c53f04194d1247c6eebdaab7c610cf7d66709b3b`

# 3: Push image 过程

> 先推各个 Layer 层到 registry 仓库，然后上传清单 Manifest

## 3.1 Pushing a Layer（上传层）

上传层分为两步，第一步使用 post 请求在 registry 仓库启动上传服务
，返回一个 url，这个 url 可以用来上传数据和检查状态。

### 3.1.1 Existing Layers(检查层是否存在)

- **API**
  `>>> HEAD /v2/<name>/blobs/<digest>`
- **Return**
  `若返回200 OK则表示存在，不用上传`

### 3.1.2 Starting An Upload(启动上传服务)

- **API**
  `>>> POST /v2/<name>/blobs/uploads/`
- **Return**
  如果 post 请求返回 202 accepted，一个 url 会在 location 字段返回.
  ```bash
  202 Accepted
  Location: /v2/<name>/blobs/uploads/<uuid>
  Range: bytes=0-<offset>
  Content-Length: 0
  Docker-Upload-UUID: <uuid> # 可以用来查看上传状态和实现断点续传
  ```

### 3.1.3 Uploading the Layer(上传层)

#### 3.1.3.1 Upload Progress(上传进度)

- **API**
  ```bash
  >>> GET /v2/<name>/blobs/uploads/<uuid>
  >>> Host: <registry host>
  ```
- **Return**
  ```bash
  204 No Content
  Location: /v2/<name>/blobs/uploads/<uuid>
  Range: bytes=0-<offset>
  Docker-Upload-UUID: <uuid>
  ```

#### 3.1.3.2 Monolithic Upload(整块上传）

- **API**
  ```bash
  >>> PUT /v2/<name>/blobs/uploads/<uuid>?digest=<digest>
  >>> Content-Length: <size of layer>
  >>> Content-Type: application/octet-stream
  <Layer Binary Data>
  ```
- **Return**

  ```bash

  ```

#### 3.1.3.3 Chunked Upload（分块上传）

- **API**
  ```bash
  >>> PATCH /v2/<name>/blobs/uploads/<uuid>
  >>> Content-Length: <size of chunk>
  >>> Content-Range: <start of range>-<end of range>
  >>> Content-Type: application/octet-stream
  <Layer Chunk Binary Data>
  ```
- **Return**

  - 如果服务器不接受这个块，则返回：

  ```bash
  416 Requested Range Not Satisfiable
  Location: /v2/<name>/blobs/uploads/<uuid>
  Range: 0-<last valid range>
  Content-Length: 0
  Docker-Upload-UUID: <uuid>
  ```

  - 成功返回：

  ```bash
  202 Accepted
  Location: /v2/<name>/blobs/uploads/<uuid>
  Range: bytes=0-<offset>
  Content-Length: 0
  Docker-Upload-UUID: <uuid>
  ```

#### 3.1.3.4 Completed Upload(上传完成)

> 分块上传在最后一块上传完毕后，需要提交一个上传完成的请求.

- **API**
  ```bash
  >>> PUT /v2/<name>/blob/uploads/<uuid>?digest=<digest>
  >>> Content-Length: <size of chunk>
  >>> Content-Range: <start of range>-<end of range>
  >>> Content-Type: application/octet-stream
  <Last Layer Chunk Binary Data>
  ```
- **Return**

  ```bash
  201 Created
  Location: /v2/<name>/blobs/<digest>
  Content-Length: 0
  Docker-Content-Digest: <digest>
  ```

#### 3.1.3.5 Canceling an Upload(取消上传)

> 这个请求执行后 uuid 将失效，当上传超时或者没有完成，客户端都应该发送这个请求。

- **API**
  ```bash
  >>> DELETE /v2/<name>/blobs/uploads/<uuid>
  ```
- **Return**

#### 3.1.3.6 Cross Repository Blob Mount（交叉挂载层）

> 此 api 可把客户端有访问权限的已有存储库中的层挂载到当前储存库中。

- **API**
  ```bash
  >>> POST /v2/<name>/blobs/uploads/?mount=<digest>&from=<repository name>
  Content-Length: 0
  ```
- **Return**
  - 成功返回:
  ```bash
  201 Created
  Location: /v2/<name>/blobs/<digest>
  Content-Length: 0
  Docker-Content-Digest: <digest>
  ```
  - 失败返回:
  ```bash
  202 Accepted
  Location: /v2/<name>/blobs/uploads/<uuid>
  Range: bytes=0-<offset>
  Content-Length: 0
  Docker-Upload-UUID: <uuid>
  ```

## 3.2 Deleting a Layer(删除层)

- **API**
  ```bash
  >>> DELETE /v2/<name>/blobs/<digest>
  ```
- **Return**
  - 成功返回:

```bash
202 Accepted
Content-Length: None
```

- 失败返回 404:

## 3.3 Pushing an Image Manifest（上传镜像清单）

> 当镜像层上传完毕后，可以上传清单。

- **API**
  ```bash
  >>> PUT /v2/<name>/manifests/<reference>
  Content-Type: <manifest media type>
  {
   "name": <name>,
   "tag": <tag>,
   "fsLayers": [
      {
         "blobSum": <digest>
      },
      ...
    ]
   ],
   "history": <v1 images>,
   "signature": <JWS>,
   ...
  }
  ```
- **Return**

  - 如果清单中有层是未知的，则返回：

  ```bash
  {
  "errors:" [{
         "code": "BLOB_UNKNOWN",
         "message": "blob unknown to registry",
         "detail": {
             "digest": <digest>
         }
     },
     ...
  ]
  }
  ```

# 4: Pull image 过程

## 4.1 Pulling an Image Manifest（拉取镜像清单）

- **API**

  ```bash
  >>> HEAD /v2/<name>/manifests/<reference> #检查镜像清单是否存在
  >>> GET /v2/<name>/manifests/<reference>  #拉取镜像清单

  # Note: reference可以是tag或者是digest
  ```

## 4.2 Pulling a Layer（拉取层）

- **API**

  ```bash
  >>> GET /v2/<name>/blobs/<digest>
  ```

# 5: Retrieve 检索功能

## 5.1 Listing Repositories（列出存储库）

- **API**
  ```bash
  >>> GET /v2/_catalog
  ```
- **Return**
  ```bash
  200 OK
  Content-Type: application/json
  {
  "repositories": [
    <name>,
    ...
  ]
  }
  ```

## 5.2 Pagination(部分列出存储库)

- **API**

  ```bash
  >>> GET /v2/_catalog?n=<integer>

  # Note : integer表示要列出库的个数
  ```

- **Return**
  ```bash
  200 OK
  Content-Type: application/json
  Link: <<url>?n=<n from the request>&last=<last repository in response>>; rel="next"
  {
  "repositories": [
    <name>,
    ...
  ]
  }
  ```

## 5.3 Listing Image Tags(列出镜像 tag)

- **API**

  ```bash
  >>> GET /v2/<name>/tags/list
  ```

- **Return**

  ```bash
  200 OK
  Content-Type: application/json
  {
    "name": <name>,
    "tags": [
        <tag>,
        ...
    ]
  }
  ```

## 5.4 Pagination(部分列出镜像 tag)

- **API**

  ```bash
  >>> GET /v2/<name>/tags/list?n=<integer>
  ```

- **Return**

  ```bash
  200 OK
  Content-Type: application/json
  Link: <<url>?n=<n from the request>&last=<last tag value from previous response>>; rel="next"
  {
  "name": <name>,
  "tags": [
    <tag>,
    ...
  ]
  }
  ```

# 6: Deleteing an Image（删除镜像）

- **API**

  ```bash
  >>> DELETE /v2/<name>/manifests/<reference>
  ```

- **Return**
  - 成功
  ```bash
  202 Accepted
  Content-Length: None
  ```
  - 失败返回 404

# 7: Errors 错误信息

- 通过 API 遇到的错误代码列举在下表中：

| Code 错误类型           | Message                                        | Description                                                                                                                                                                                                                 | Others |
| ----------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| `BLOB_UNKNOWN`          | blob unknown to registry                       | 当指定存储库中的注册表未知 blob 时，可能会返回此错误。可以使用标准 get 返回，或者如果清单在上载期间引用了未知层。                                                                                                           |        |
| `BLOB_UPLOAD_INVALID`   | blob upload invalid                            | blob 上载遇到错误，无法继续                                                                                                                                                                                                 |        |
| `BLOB_UPLOAD_UNKNOWN`   | blob upload unknown to registry                | 如果 blob 上载 cancelled 或从未启动，则可能会返回此错误代码                                                                                                                                                                 |        |
| `DIGEST_INVALID`        | provided digest did not match uploaded content | 当上传 blob 时，注册表将检查内容是否与客户端提供的 digest 匹配。错误可能包括一个带有 key `digest`的 detail structure，包括无效的摘要字符串。当清单包含无效的层摘要时，也可能返回此错误                                      |        |
| `MANIFEST_BLOB_UNKNOWN` | blob unknown to registry                       | This error may be returned when a manifest blob is unknown to the registry.                                                                                                                                                 |        |
| `MANIFEST_INVALID`      | manifest invalid                               | During upload, manifests `undergo several checks ensuring validity`. If those checks fail, this error may be returned, unless a more specific error is included. The detail will contain information the failed validation. |        |
| `MANIFEST_UNKNOWN`      | manifest unknown                               | This error is returned when the manifest, identified by name and tag is unknown to the repository.                                                                                                                          |        |
| `MANIFEST_UNVERIFIED`   | manifest failed signature verification         | During manifest upload, if the manifest fails signature verification, this error will be returned.                                                                                                                          |        |
| `NAME_INVALID`          | invalid repository name                        | 在 manifest 验证期间或者任何 API 操作期间遇到了无效的 repository name                                                                                                                                                       |        |
| `NAME_UNKNOWN`          | repository name not known to registry          | 如果 registry 注册表不知道操作过程中使用的名称，则返回此值                                                                                                                                                                  |        |
| `SIZE_INVALID`          | provided length did not match content length   | When a layer is uploaded, the provided size will be checked against the uploaded content. If they do not match, this error will be returned.                                                                                |        |
| `TAG_INVALID`           | manifest tag did not match URI                 |                                                                                                                                                                                                                             |        |
| `UNAUTHORIZED`          | authentication required                        | 访问控制器(access controller)无法验证客户端。通常，这会伴随一个 `Www Authenticate HTTP` 响应头，指示如何进行身份验证                                                                                                        |        |
| `DENIED`                | requested access to the resource is denied     |                                                                                                                                                                                                                             |        |
| `UNSUPPORTED`           |                                                | The operation was unsupported _due to_ a missing implementation or invalid set of parameters.                                                                                                                               |        |

备注:参考https://blog.csdn.net/ztsinghua/article/details/51496658
