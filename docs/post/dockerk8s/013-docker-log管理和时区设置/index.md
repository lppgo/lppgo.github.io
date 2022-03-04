
<div align="center"><font size="35">docker log管理和时区设置</font></div>

- [1：docker log](#1docker-log)
  - [1.1 docker log Description](#11-docker-log-description)
  - [1.2 磁盘占用分析](#12-磁盘占用分析)
    - [1.2.1 **df -ah** 查看系统中文件的使用情况](#121-df--ah-查看系统中文件的使用情况)
    - [1.2.2 **du -sh** 查看当前目录下各个文件及目录占用空间大小](#122-du--sh-查看当前目录下各个文件及目录占用空间大小)
    - [1.2.3 df -h 和 du -sh 显示的磁盘大小不一致原因及解决办法](#123-df--h-和-du--sh-显示的磁盘大小不一致原因及解决办法)
  - [1.3 docker log 管理](#13-docker-log-管理)
- [2：关于 TimeZone 时区问题](#2关于-timezone-时区问题)
  - [2.1 通过传递环境变量改变容器时区](#21-通过传递环境变量改变容器时区)
  - [2.2 在 docker-compose 编排时指定环境变量](#22-在-docker-compose-编排时指定环境变量)
  - [2.3 彻底的解决时区问题，通过 dockerfile 重新制作镜像](#23-彻底的解决时区问题通过-dockerfile-重新制作镜像)
    - [2.3.1 Alpine](#231-alpine)
    - [2.3.2 Debian](#232-debian)
    - [2.3.3 Ubuntu](#233-ubuntu)
    - [2.3.4 CentOS](#234-centos)

# 1：docker log

## 1.1 docker log Description

- docker 的日志分为两种，第一种是 docker 引擎的日志，第二种是 docker 容器运行时的服务日志，默认为 json-file 格式;
- json-file 日志驱动 记录从容器的 STOUT/STDERR 的输出 ，用 JSON 的格式写到文件中，日志中不仅包含着 输出日志，还有时间戳和 输出格式.
- docker 所有的日志驱动如下：
  |日志驱动|description|others|
  |:---|:---|:---|
  |none|运行的容器没有日志，docker logs 也不返回任何输出||
  |local|日志以自定义格式存储，旨在实现最小开销| |
  |json-file|日志格式为 JSON,Docker 的默认日志记录驱动程序| |
  |syslog|将日志消息写入 syslog。该 syslog 守护程序必须在主机上运行| |
  |journald|将日志消息写入 journald。该 journald 守护程序必须在主机上运行| |
  |gelf|将日志消息写入 Graylog 扩展日志格式（GELF）端点，例如 Graylog 或 Logstash| |
  |fluentd|将日志消息写入 fluentd（转发输入）。该 fluentd 守护程序必须在主机上运行| |
  |awslogs|将日志消息写入 Amazon CloudWatch Logs| |
  |splunk|使用 HTTP 事件收集器将日志消息写入 splunk| |
  |etwlogs|将日志消息写为 Windows 事件跟踪（ETW）事件。仅适用于 Windows 平台| |
  |gcplogs|将日志消息写入 Google Cloud Platform（GCP）Logging| |
  |logentries|将日志消息写入 Rapid7 Logentries| |
- 常用的驱动是 `json-file`，`syslog` ,`journald` 这三种，json-file 是默认的日志驱动;
- docker 的日志通常默认是保存在 /var/lib/docker/containers/容器 ID/ 目录下,日志文件名称为 **容器 ID-json-log**,当然，docker 日志也有级别，通常级别为 info。

## 1.2 磁盘占用分析

### 1.2.1 **[df -ah]()** 查看系统中文件的使用情况

- **df** （disk free） 检查文件系统占用磁盘情况；

```json
Size 分割区总容量
Used 已使用的大小
Avail 剩下的大小
Use% 使用的百分比
Mounted on 路径地址
```

### 1.2.2 **[du -sh]()** 查看当前目录下各个文件及目录占用空间大小

- **du** （disk usage） 检查目录占用磁盘情况；

```json
du -h --max-depth=1 /root/* 查看目录下的所有文件大小
du -h --max-depth=1 /root 列出root目录下面所有的一级目录文件大小；
```

### 1.2.3 df -h 和 du -sh 显示的磁盘大小不一致原因及解决办法

- **原因** du 是根据文件名进行的空间统计，使用 rm 时该文件对系统来说已经不可见，所以不会统计这个文件。
  df 则是磁盘实际占用的数量
- `du -h /var/lib/docker/`
- `df -h /var/lib/docker/`
- **解决办法**
  - (1/2) lsof 查看使用文件的进程，结束进程。
    - `lsof | grep test.log`
    - `ps aux | grep 28600`
    - `kill -9 28600`
  - (2/2) 或使用清空的方式代替 rm，如 [echo > /tmp/test.log]()
    - 日志文件清空一般不是删除 rm 命令，而是 > 文件名这样的清空方式.

## 1.3 docker log 管理

- 日志文件清空一般不是删除 rm 命令，而是 > 文件名这样的清空方式；
- docker 日志野蛮增长的情况应该如何处理呢？

  - 第一，定时任务清空日志,但治标不治本；
  - 第二，限制日志的大小，指定日志只能多大，修改 docker `daemon.json`;
  - 第三，更改 docker 的工作目录到一个磁盘空间多的分区;

    - (1) vim /etc/systemd/system/docker.service

      ```json
      // stop docker

      // vim /etc/systemd/system/docker.service
      ExecStart=/usr/local/bin/dockerd --graph=/opt/docker

      // 重启docker
      ```

    - (2) **/etc/docker/daemon.json**

      ```json
      {
        "log-driver": "json-file",
        "log-opts": { "max-size": "500m", "max-file": "3" }
      }
      ```

    - (3) **容器 run 时单独限制**. `--log-driver json-file --log-opt max-size=10m`，比如，将这一段加在 docker run 后面，那么以这条命令启动的容器日志将会限定在 10m 大小，并且使用的日志驱动是 json-file;
    - (4) **docker-compose 编排文件限制** :
      ```json
      nginx:
          image: nginx:1.12.1
          restart: always
          logging:
              driver: “json-file”
              options:
              max-size: “2g”
      ```

# 2：关于 TimeZone 时区问题

- 时区问题是大问题，时间没统一好，业务会乱套。究其原因，大部分 Docker 镜像都是基于 Alpine，Ubuntu，Debian，CentOS 等基础镜像制作而成。基本上都采用 UTC 时间，默认时区为零时区.

## 2.1 通过传递环境变量改变容器时区

- 适用于基于 Debian 基础镜像, CentOS 基础镜像 制作的 Docker 镜像
- 不适用于基于 Alpine 基础镜像, Ubuntu 基础镜像 制作的 Docker 镜像

```json
root@centos11 ~]# docker run -it --name mysql2 -e TZ=Asia/Shanghai -e MYSQL_ROOT_PASSWORD=12345 -p 3306:3306 hub.c.163.com/library/mysql /bin/bash
root@d0d8ba4c6135:/# date
Sat Jan 23 16:31:39 CST 2021
root@d0d8ba4c6135:/# exit
[root@centos11 ~]# docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED             SIZE
hub.c.163.com/library/mysql   latest              9e64176cd8a2        3 years ago         407M
```

## 2.2 在 docker-compose 编排时指定环境变量

- 同样的只适用于 debian 系列操作系统镜像;
  ```yaml
  version: "3"
  services:
  mysql:
    container_name: mysql_57
    image: hub.c.163.com/library/mysql:5.7.18
    restart: always
    environment:
    MYSQL_USER: admin
    MYSQL_PASSWORD: admins
    MYSQL_DATABASE: database
    MYSQL_ROOT_PASSWORD: admin
    TZ: Asia/Shanghai
    volumes:
      - /usr/local/mysql/data:/var/lib/mysql
    ports:
      - 3306:3306
    network_mode: host
  ```

## 2.3 彻底的解决时区问题，通过 dockerfile 重新制作镜像

### 2.3.1 Alpine

```yml
ENV TZ Asia/Shanghai

RUN apk add tzdata && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
&& echo ${TZ} > /etc/timezone \
&& apk del tzdata
```

### 2.3.2 Debian

```yml
ENV TZ=Asia/Shanghai \
DEBIAN_FRONTEND=noninteractive

RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
&& echo ${TZ} > /etc/timezone \
&& dpkg-reconfigure --frontend noninteractive tzdata \
&& rm -rf /var/lib/apt/lists/*
```

### 2.3.3 Ubuntu

- Ubuntu 基础镜像中没有安装了 tzdata 包，因此我们需要先安装 tzdata 包;

  ```yml
  ENV TZ=Asia/Shanghai \
  DEBIAN_FRONTEND=noninteractive

  RUN apt update \
  && apt install -y tzdata \
  && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
  && echo ${TZ} > /etc/timezone \
  && dpkg-reconfigure --frontend noninteractive tzdata \
  && rm -rf /var/lib/apt/lists/*
  ```

### 2.3.4 CentOS

- CentOS 基础镜像 中已经安装了 tzdata 包，我们可以将以下代码添加到 Dockerfile 中;

  ```yaml
  ENV TZ Asia/Shanghai

  RUN ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
  && echo ${TZ} > /etc/timezone
  ```
