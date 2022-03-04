---
title: "01-Grpc with TLS/SSL"
author: "lucas"
date: 2021-12-17
lastmod: 2021-12-17

tags: ["GRPC"]
categories: ["Go", "CPP"]
keywords: ["grpc"]
---

<div align="center"><font size="35">Grpc with TLS/SSL</font></div>

- [1 Grpc 配置 TLS/SSL](#1-grpc-配置-tlsssl)
  - [1.1 使用 openssl 生成证书 cert](#11-使用-openssl-生成证书-cert)
- [2 Server 服务端](#2-server-服务端)
- [3 Client 客户端](#3-client-客户端)

# 1 Grpc 配置 TLS/SSL

gRPC 支持身份验证（auth）。将它添加到您的项目中很简单。您所要做的就是使用几行代码对其进行配置。gRPC 支持的身份验证类型之一是 SSL/TLS。

## 1.1 使用 openssl 生成证书 cert

- (1) 使用 openssl 直接生成

```bash
openssl genrsa -aes256 -passout pass:gsahdg -out server.pass.key 4096
openssl rsa -passin pass:gsahdg -in server.pass.key -out server.key
openssl req -new -key server.key -out server.csr

# and generate the certificate
openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt
```

- (2) 如果遇到以下错误

  ```bash
  transport: x509: certificate is not valid for any names, but wanted to match localhost:8070
  ```

  问题是您需要证书颁发机构。我找到了一种更好、更简单的解决方法。当然，我们可以使用 openssl 来做到这一点，但我喜欢非常简单的解决方案，几乎没有犯错的余地。另一个解决方案不需要 openssl！您所要做的就是安装[certstrap](https://github.com/square/certstrap)。也许这不是世界上最安全的事情，但对于本地开发而言，IMO 比使用 openssl 更简单。

- (3) 要生成证书颁发机构，生成证书并对其进行签名，您可以使用以下命令：
  ```go
    certstrap init --common-name "developer20.com"
    certstrap request-cert -domain localhost
    certstrap sign localhost --CA developer20.com
  ```

# 2 Server 服务端

从服务器端来看，代码如下所示：

```go
creds, err := credentials.NewServerTLSFromFile(certFile, keyFile)
if err != nil {
    // handle the error - no ignore it!
}
s := grpc.NewServer(grpc.Creds(creds))
```

https://grpc.io/docs/languages/cpp/quickstart/

# 3 Client 客户端

客户端代码，如下所示：

```go
creds, err := credentials.NewClientTLSFromFile(certFile, "")
if err != nil {
    // handle the error - no ignore it!
}
conn, _ := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(creds))
```
