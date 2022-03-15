---
title: "01-Go Dockerfile"
author: "lucas"
date: 2022-03-10
lastmod: 2022-03-10

categories: ["Go"]
tags: ["docker"]
keywords: ["dockerfile"]
---

<div align="center"><font size="35">Go Dockerfile模板</font></div>

# 1：

```dockerfile
FROM golang:alpine AS builder

LABEL stage=gobuilder

ENV CGO_ENABLED 0
ENV GOOS linux
ENV GOPROXY https://goproxy.cn,direct

WORKDIR /build

ADD go.mod .
ADD go.sum .
RUN go mod download
COPY . .
RUN go build -ldflags="-s -w" -o /app/hello ./hello.go


FROM alpine

RUN apk update --no-cache && apk add --no-cache ca-certificates tzdata
ENV TZ Asia/Shanghai

WORKDIR /app
COPY --from=builder /app/hello /app/hello

CMD ["./hello"]


```

# 2: 说明

- 默认禁用了 cgo
- 启用了 GOPROXY
- 去掉了调试信息 -ldflags="-s -w" 以减小镜像尺寸
- 安装了 ca-certificates，这样使用 TLS 证书就没问题了
- 自动设置了本地时区，这样我们在日志里看到的是北京时间了
