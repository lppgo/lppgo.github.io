---
title: "01-WSL2中配置docker远程tcp"
author: "lucas" # 文章作者
description: "WSL2中配置docker远程tcp" # 文章描述信息
date: 2021-07-27T14:58:35+08:00
lastmod: 2021-07-27T14:58:35+08:00

tags: # 文章所属标签
  ["wsl2", "docker"]
categories: # 文章所属目录
  ["Docker"]
keywords: # 文章关键词
  ["wsl2", "docker"]
---

<div align='center' ><font size='50'>WSL2中配置docker远程tcp</font></div>

<!-- [toc] -->

- [1: 修改 `/lib/systemd/system/docker.service`](#1-修改-libsystemdsystemdockerservice)
- [2: 设置 `DOCKER_HOST` 环境变量](#2-设置-docker_host-环境变量)
- [3: 修改 docker 启动配置文件`/etc/default/docker`](#3-修改-docker-启动配置文件etcdefaultdocker)
- [4: 重启 docker](#4-重启-docker)

---

# 1: 修改 `/lib/systemd/system/docker.service`

```bash
# sudo vim /lib/systemd/system/docker.service

[Service]
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock -H fd:// --containerd=/run/containerd/containerd.sock
# 上面这一行,主要是增加了`-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock`

```

# 2: 设置 `DOCKER_HOST` 环境变量

```bash
# sudo vim ~/.zshrc
export DOCKER_HOST=tcp://0.0.0.0:2375

source ~/.zshrc
```

# 3: 修改 docker 启动配置文件`/etc/default/docker`

```bash
# 开启远程访问 -H tcp://0.0.0.0:2375
# 开启本地套接字访问 -H unix:///var/run/docker.sock
DOCKER_OPTS="-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"
```

# 4: 重启 docker

```bash
sudo service docker restart
```
