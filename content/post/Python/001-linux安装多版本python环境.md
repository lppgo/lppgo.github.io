---
title: "001-linux安装多版本python环境"
author: "lucas"
description: "..."
date: 2022-08-08
lastmod: 2021-08-08

tags: ["Python", "update-alternatives"]
categories: ["Python"]
keywords: ["python"]
---

- [1：简介](#1简介)
- [2：Linux 安装多个版本 python](#2linux-安装多个版本-python)
  - [2.1 下载 python 安装包](#21-下载-python-安装包)
  - [2.2 update-alternative 管理多版本 python](#22-update-alternative-管理多版本-python)
  - [2.3 创建软连接](#23-创建软连接)
- [3: pip 源设置](#3-pip-源设置)

# 1：简介

使用源码安装多个版本 python 环境，对系统原有 py 不影响

# 2：Linux 安装多个版本 python

## 2.1 下载 python 安装包

- [python.org](https://www.python.org/): 速度慢
- [https://registry.npmmirror.com/binary.html](https://registry.npmmirror.com/binary.html?path=python/):国内镜像

```go
// ---------- python3.8 源码安装 --------------
// (1) 创建安装目录
mkdir -p /usr/local/python/python3.8
cd /usr/local/python/python3.8
// (2) 下载源码包
sudo wget  https://registry.npmmirror.com/-/binary/python/3.8.13/Python-3.8.13.tgz
tar -zxvf Python-3.8.13.tgz
cd Python-3.8.13
// (3) 配置要安装的目录
./configure prefix=/usr/local/python/python3.8 --enable-optimizations
// (4) 编译源码
sudo make -j8
// (5) make altinstall与make install的区别，altinstall skips creating the python link and the manual pages links
// https://blog.csdn.net/andylauren/article/details/108363030
sudo make altinstall



// python3.10
mkdir -p /usr/local/python/python3.10
cd /usr/local/python/python3.10
sudo wget https://registry.npmmirror.com/-/binary/python/3.10.6/Python-3.10.6.tgz
```

## 2.2 update-alternative 管理多版本 python

> update-alternatives 命令用于处理 linux 系统中软件版本的切换

```go
// 注册软件
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/python/python3.8/bin/python3.8  38
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/python/python3.10/bin/python3.10  40

// 查看已注册列表
update-alternatives --display python

// manual修改
update-alternatives --config python

// 清理注册
update-alternatives --remove python /usr/local/python/python3.8/bin/python3.8
update-alternatives --remove-all python

```

## 2.3 创建软连接

```go
// python
ln -s /usr/local/python3.8/bin/python3.8 /usr/bin/python38


// pip
ln -s /usr/local/python3.8/bin/pip3.8 /usr/bin/pip38
```

# 3: pip 源设置

- `~/.pip/pip.conf`

```go
# 写入以下内容配置阿里镜像源
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com

# 写入以下内容则配置华为镜像源
# [global]
# index-url = https://mirrors.huaweicloud.com/repository/pypi/simple
# trusted-host = mirrors.huaweicloud.com


timeout = 120
```
