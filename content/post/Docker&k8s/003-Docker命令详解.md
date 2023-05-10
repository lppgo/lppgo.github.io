---
title: "01-Docker命令详解.md"
author: "lucas"
date: 2021-05-31
lastmod: 2021-05-31

tags: ["Docker"]
categories: ["Docker"]
keywords: ["Docker", "容器"]
---

# Table of Contents

- [1: docker](#1-docker)
- [2: docker 的使用命令](#2-docker的使用命令)
  - [2.1 docker --help](#21-docker---help)
  - [2.2 docker build](#22-docker-build)
  - [2.3 docker run](#23-docker-run)
  - [2.4 保存和加载镜像](#24-保存和加载镜像)
- [3: docker Container](#3-docker-container)
- [4: docker Network](#4-docker-network)
- [5: docker volume](#5-docker-volume)
- [6: 发布镜像](#6-发布镜像)
- [7: Dockerfile](#7-dockerfile)
- [8: other](#8-other)

# 1: docker

- 容器技术
- image
- container
- repository

```bash
# 1: pdocker ps 显示过长问题：
docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}"

docker ps | less -S

# 2: docker如何将容器内文件复制到本地
docker container cp -a c56d9375ff28:/etc/kraken ./

# 3:
CMD: 指定容器被启动时要运行的命令
ENTRYPOINT: 同 CMD ,但不会被 docker run -t 覆盖
```

# 2: docker 的使用命令

## 2.1 docker --help

```bash
docker --help

管理命令:
  container   管理容器
  image       管理镜像
  network     管理网络
命令：
  attach      介入到一个正在运行的容器
  build       根据 dockerfile 构建一个镜像
  commit      根据容器的更改创建一个新的镜像
  cp          在本地文件系统与容器中复制 文件/文件夹
  create      创建一个新容器
  exec        在容器中执行一条命令
  images      列出镜像
  kill        杀死一个或多个正在运行的容器
  logs        取得容器的日志
  pause       暂停一个或多个容器的所有进程
  ps          列出所有容器
  pull        拉取一个镜像或仓库到 registry
  push        推送一个镜像或仓库到 registry
  rename      重命名一个容器
  restart     重新启动一个或多个容器
  rm          删除一个或多个容器
  rmi         删除一个或多个镜像
  run         在一个新的容器中执行一条命令
  search      在 Docker Hub 中搜索镜像
  start       启动一个或多个已经停止运行的容器
  stats       显示一个容器的实时资源占用
  stop        停止一个或多个正在运行的容器
  tag         为镜像创建一个新的标签
  top         显示一个容器内的所有进程
  unpause     恢复一个或多个容器内所有被暂停的进程
```

## 2.2 docker build

```bash
命令格式：docker build [OPTIONS] <PATH | URL | ->
Usage: Build an image from a Dockerfile.
常用选项说明

--build-arg       设置构建时的变量
--no-cache        默认false。设置该选项，将不使用Build Cache构建镜像
--pull            默认false。设置该选项，总是尝试pull镜像的最新版本
--compress        默认false。设置该选项，将使用gzip压缩构建的上下文
--disable-content-trust 默认true。设置该选项，将对镜像进行验证
--file, -f        Dockerfile的完整路径，默认值为‘PATH/Dockerfile’
--isolation       默认--isolation="default"，即Linux命名空间；其他还有process或hyperv
--label           为生成的镜像设置metadata
--squash          默认false。设置该选项，将新构建出的多个层压缩为一个新层，但是将无法在多个镜像之间共享新层；设置该选项，实际上是创建了新image，同时保留原有image。
--tag, -t         镜像的名字及tag，通常name:tag或者name格式；可以在一次构建中为一个镜像设置多个tag
--network         默认default。设置该选项，Set the networking mode for the RUN instructions during build
--quiet, -q       默认false。设置该选项，Suppress the build output and print image ID on success
--force-rm        默认false。设置该选项，总是删除掉中间环节的容器
--rm，默认--rm=true 即整个构建过程成功后删除中间环节的容器

```

> 示例

`docker build -t bjc/demo:latest --rm .`

- -t bjc/demo:latest，为构建的镜像标记名称，即镜像名为：bjc/demo，打标为 latest；
- --rm，整个构建过程成功后删除中间环节的容器；`.`，单独的点，意思为根据当前目录下的 Dockerfile 文件生成镜像

## 2.3 docker run

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

-d, --detach=false， 指定容器运行于前台还是后台，默认为false
-i, --interactive=false， 打开STDIN，用于控制台交互
-t, --tty=false， 分配tty设备，该可以支持终端登录，默认为false
-u, --user=""， 指定容器的用户
-a, --attach=[]， 登录容器（必须是以docker run -d启动的容器）
-w, --workdir=""， 指定容器的工作目录
-c, --cpu-shares=0， 设置容器CPU权重，在CPU共享场景使用
-e, --env=[]， 指定环境变量，容器中可以使用该环境变量
-m, --memory=""， 指定容器的内存上限
-P, --publish-all=false， 指定容器暴露的端口
-p, --publish=[]， 指定容器暴露的端口
-h, --hostname=""， 指定容器的主机名
-v, --volume=[]， 给容器挂载存储卷，挂载到容器的某个目录
--volumes-from=[]， 给容器挂载其他容器上的卷，挂载到容器的某个目录
--cap-add=[]， 添加权限，权限清单详见：http://linux.die.net/man/7/capabilities
--cap-drop=[]， 删除权限，权限清单详见：http://linux.die.net/man/7/capabilities
--cidfile=""， 运行容器后，在指定文件中写入容器PID值，一种典型的监控系统用法
--cpuset=""， 设置容器可以使用哪些CPU，此参数可以用来容器独占CPU
--device=[]， 添加主机设备给容器，相当于设备直通
--dns=[]， 指定容器的dns服务器
--dns-search=[]， 指定容器的dns搜索域名，写入到容器的/etc/resolv.conf文件
--entrypoint=""， 覆盖image的入口点
--env-file=[]， 指定环境变量文件，文件格式为每行一个环境变量
--expose=[]， 指定容器暴露的端口，即修改镜像的暴露端口
--link=[]， 指定容器间的关联，使用其他容器的IP、env等信息
--lxc-conf=[]， 指定容器的配置文件，只有在指定--exec-driver=lxc时使用
--name=""， 指定容器名字，后续可以通过名字进行容器管理，links特性需要使用名字
--net="bridge"， 容器网络设置:
    bridge 使用docker daemon指定的网桥
    host //容器使用主机的网络
    container:NAME_or_ID >//使用其他容器的网路，共享IP和PORT等网络资源
    none 容器使用自己的网络（类似--net=bridge），但是不进行配置
--privileged=false， 指定容器是否为特权容器，特权容器拥有所有的capabilities
--restart="no"， 指定容器停止后的重启策略:
    no：容器退出时不重启
    on-failure：容器故障退出（返回值非零）时重启
    always：容器退出时总是重启
--rm=false， 指定容器停止后自动删除容器(不支持以docker run -d启动的容器)
--sig-proxy=true， 设置由代理接受并处理信号，但是SIGCHLD、SIGSTOP和SIGKILL不能被代理

```

## 2.4 保存和加载镜像

```bash

ocker save -o mysql.8.0.25.tar mysql:8.0.25

docker load -i mysql.8.0.25.tar
```

# 3: docker Container

```bash
# ls
docker container ls # -a

# rm
docker container rm <containerID> # -f  强制删除; <name>

# top 查询容器中的进程
#查询指定containerID的Container进程详情
docker container top <containID> # <name>

# inspect
docker container inspect <containID>

# 查看指定docker内网ip
docker container insepct --format '{{.NetworkSettings.IPAddress}}' <name>

# stats 查询所有容器的状态
docker container stats <containID>

# exec在container中执行命令
docker container exec -it <container_name> <command_to_exec>

```

# 4: docker Network

```bash
# 1: ls显示所有网络
docker network ls

# 2: inspect查看网络具体信息
docker network inspect <network_name>

# 3：create创建网络
docker network create <custom_network_name>

# 4：连接指定网络到容器
docker network connect <network_id> <container_id>
docker network disconnect <network_id> <container_id>

```

# 5: docker volume

```bash
# 1.ls 查询所有volume列表
docker volume ls

# 2.rm 删除指定volume
docker volume rm <volume_name>

# 3.inspect 查询volume信息
docker volume inspect <volume_name>

# 4.prune 删除所有未使用的本地数据卷
docker volume inspect <volume_name>

# 5.create 创建数据卷
docker volume create <volume_name>

```

# 6: 发布镜像

```bash

docker login

docker push new-image-name
```

# 7: Dockerfile

# 8: other

- [dozzle](https://github.com/amir20/dozzle): docker 容器 log 实时查看的工具。
