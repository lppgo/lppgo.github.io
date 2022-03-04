---
title: "02-Windows & WSL2 代理学习记录"
author: "lucas" # 文章作者
description: "记录 windows proxy..." # 文章描述信息
date: 2021-04-13T17:16:49+08:00
lastmod: 2021-04-13T17:16:49+08:00

tags: # 文章所属标签
  ["Proxy"]
categories: # 文章所属目录
  ["Linux"]
keywords: # 文章关键词
  ["WSL2 代理", "Windows 代理"]
# prev: ./20210413-01.md # 上一篇博客地址

# next: ./20210414-01.md # 下一篇博客地址
---

- [Windows WSL2 代理学习记录](#windows-wsl2-代理学习记录)
  - [1: Proxy 服务](#1-proxy-服务)
  - [2: 客户端](#2-客户端)
  - [3: 在 Windows 设置 proxy](#3-在-windows-设置-proxy)
  - [4: 在 WSL2 设置 proxy，使用宿主机代理](#4-在-wsl2-设置-proxy使用宿主机代理)

# Windows WSL2 代理学习记录

## 1: Proxy 服务

楼主用的 monocloud,用了 3 年，感觉很稳定，很好用。
特点就是稳定，便宜，速度很快(看 p 站某油管 1080 就和本地差不多)，有加速服务。
需要邀请码请联系我 1605577372@qq.com

## 2: 客户端

使用的都是网站推荐到 Client，跨平台，都有说明，使用简单。
![数据结构图谱](/images/微信截图_20210413193319.png)
1: 使用网站的 MonoCloud 客户端
2: 使用网站推荐的 [Clashy](https://mymonocloud.com/knowledgebase/16)

## 3: 在 Windows 设置 proxy

1: 按照说明配置 Client，设置好端口
2: Windows10 系统设置手动代理，比如 127.0.0.1：7078
3: 在 Chrome 浏览器访问www.google.com 测试是否正常访问
4: 在 cmd 设置 proxy，使用 curl 命令访问测试

```go
1: 在cmd 设置proxy
set http_proxy=http://127.0.0.1:7078
set https_proxy=http://127.0.0.1:7078

2: 在cmd输入测试
curl http://www.google.com
```

5: 在 gitbash 设置 proxy

```go
1: 在gitbash  直接设置，临时生效
export http_proxy=http://127.0.0.1:7078
export https_proxy=http://127.0.0.1:7078

2: 在gitbash  配置文件写入上面命令
在'/c/Users/Administrator'目录打开.bashrc，写入上面命令，使用source ./.bashrc生效配置

3: 在cmd输入测试
curl http://www.google.com
```

## 4: 在 WSL2 设置 proxy，使用宿主机代理

1: 在.zshrc 写入以下命令，并用 source .zshrc 生效

```shell
export hostip=$(cat /etc/resolv.conf |grep -oP '(?<=nameserver\ ).*')
alias proxy='export http_proxy="http://${hostip}:7078";
             export https_proxy="https://${hostip}:7078";'
alias unproxy='unset http_proxy;unset https_proxy;'
```

2: 测试生效
curl http://www.google.com
