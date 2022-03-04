---
title: "01-note笔记"
author: "lucas"
draft: false
date: 2021-09-11
lastmod: 2021-09-11

tags: ["Others"]
categories: ["Others"]
keywords: ["note"]
---

<div align="center"><font size="35">note笔记</font></div>

- [1：note 文件](#1note-文件)
  - [1.1 alias 别名设置](#11-alias-别名设置)
  - [1.2 git 局部代理](#12-git-局部代理)
  - [1.3 golang 交叉编译](#13-golang-交叉编译)
  - [1.4 date 和时间戳转换](#14-date-和时间戳转换)
  - [1.5 minikube start](#15-minikube-start)
  - [1.6 ip 相关](#16-ip-相关)
  - [1.7 查看 Linux 详细 info](#17-查看-linux-详细-info)
  - [1.8 WSL2 压缩磁盘空间](#18-wsl2-压缩磁盘空间)

# 1：note 文件

## 1.1 alias 别名设置

```bash
alias gs = "git status"
alias ga = "git add -A"
alias gd = "git diff"
alias gc = "git commit -m"
```

## 1.2 git 局部代理

```bash
git clone -c http.proxy="127.0.0.1:7078" xxx
```

## 1.3 golang 交叉编译

```bash
CGO_ENABLED=0 GOOS=linux GOARCH=amd64    go build -v -a main.go

CGO_ENABLED=0 GOOS=darwin GOARCH=amd64   go build -v -a main.go

CGO_ENABLED=0 GOOS=windows GOARCH=amd64  go build -v -a main.go

# 编译时添加参数
 -ldflags "-X 'main.Version=v1.0.0' -X 'main.BuildTime=`date +"%Y-%m-%d %H:%M:%S"`' -X 'main.GoVersion=`go version`' "

```

## 1.4 date 和时间戳转换

```bash
# linux  date和时间戳转换
1：查看当前时间
date +"%Y-%m-%d %H:%M:%S"

输出："2021-03-25 18:12:38"

2：查看指定时间，转为时间戳
date +%s
date -d "2021-03-25 18:12:38" +"%Y-%m-%d %H:%M:%S"
date -d "2021-03-25 18:12:38" +%s

3：时间戳转换为date
date -d @1416387827
date -d @1416387827 +"%Y-%m-%d %H:%M:%S"
```

## 1.5 minikube start

```bash
minikube start \
    --driver docker \
    --image-mirror-country=cn \
    --registry-mirror https://3laho3y3.mirror.aliyuncs.com \
    --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers \
    --kubernetes-version=v1.20.7
```

## 1.6 ip 相关

```bash
#
curl ipinfo.io
#
curl -vv www.google.com

# ------------------查看ip--------------------
ip addr show | grep "inet"
```

## 1.7 查看 Linux 详细 info

```bash
cat /etc/*elease
```

## 1.8 WSL2 压缩磁盘空间

```bash
# ----------------------WSL2压缩磁盘空间------------------------
PowerShell，直接运行 diskpart 命令就好
select vdisk file=D:\wsl\Ubuntu-20.04\ext4.vhdx
compact vdisk


```
