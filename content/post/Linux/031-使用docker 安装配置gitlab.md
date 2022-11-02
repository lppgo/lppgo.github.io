---
title: "使用 docker 安装配置 gitlab"
author: "lucas"
date: 2022-11-02
lastmod: 2022-11-02

tags: ["Git", "gitlab"]
categories: ["Git"]
keywords: ["Git", "gitlab", "docker"]
---

<div align="center"><font size="35">使用 docker 安装配置 gitlab</font></div>

- [1: 下载 gitlab images](#1-下载-gitlab-images)
  - [2: 编写 docker-compose](#2-编写-docker-compose)
  - [3: 启动 gitlab 容器并设置 root](#3-启动-gitlab-容器并设置-root)
    - [3.1 修改配置](#31-修改配置)
    - [3.2 修改 root 密码](#32-修改-root-密码)

# 1: 下载 gitlab images

- **Gitlab**是一个开源的版本管理系统，实现一个自托管的 Git 项目仓库，可通过 Web 界面进行访问公开的或者私人项目。它拥有与 Github 类似的功能，能够浏览源码，管理缺陷和注释，可以管理团队对仓库的访问，它非常易于浏览提交的版本并提供一个文件历史库。团队成员可以利用内置的简单的聊天程序进行交流。它还提供一个代码片段收集功能可以实现代码复用。

- GitLab 对于系统性能有要求，所以我们需要将克隆出来的虚拟机的内存提高到至少 2G 以上。
- `docker pull gitlab/gitlab-ce:latest`
- `docker pull twang2218/gitlab-ce-zh:latest`
- 通过虚拟主机的 ip+端口访问，此时需要设置管理员密码，账号为 root，密码最少为 8 位

# 2: 编写 docker-compose

docker-compose-gitlab.yml

```yaml
version: "3"
services:
  web:
    image: "gitlab/gitlab-ce:latest" #gitlab镜像
    restart: always
    privileged: true #权限
    hostname: "" #主机名,即虚拟机的ip
    environment:
      TZ: "Asia/Shanghai"
      GITLAB_OMNIBUS_CONFIG: |
        external_url '' #主机名,即虚拟机的ip
        gitlab_rails['gitlab_shell_ssh_port'] = 2222
        unicorn['port'] = 8888
        nginx['listen_port'] = 8084
    ports:
      - "8084:8084"
      - "8443:443"
      - "2222:22"
    volumes:
      - "./config:/etc/gitlab"
      - "./log:/var/log/gitlab"
      - "./opt:/var/opt/gitlab"
```

# 3: 启动 gitlab 容器并设置 root

## 3.1 修改配置

- docker-compose up
- 或者进入容器 config

```bash
docker exec -it gitlab /bin/bash

#修改gitlab.rb
vi /etc/gitlab/gitlab.rb

#gitlab访问地址,可以写域名。如果端口不写的话默认为80端口
external_url 'http://47.115.218.14'
#ssh主机ip
gitlab_rails['gitlab_ssh_host'] = '47.115.218.14'
#ssh连接端口
gitlab_rails['gitlab_shell_ssh_port'] = 22

```

```bash
# 修改http和ssh配置
vi /opt/gitlab/embedded/service/gitlab-rails/config/gitlab.yml

  gitlab:
    host: 192.168.249.132
    port: 9980 # 这里改为9980
    https: false

# 在gitlab上生成的http地址应该是http://192.168.249.132:9980
```

```bash
#重启gitlab
gitlab-ctl restart
#退出容器
exit
```

- 路径访问：http://192.168.249.132:9980/
- 机器配置要大于 4g，否则很容易启动不了，报 502

## 3.2 修改 root 密码

```bash
# 进入容器内部
docker exec -it gitlab /bin/bash

# 进入控制台
gitlab-rails console -e production

# 查询id为1的用户，id为1的用户是超级管理员
user = User.where(id:1).first

user.password='Lpp19952058'
user.password_confirmation='Lpp19952058'

# 保存
user.save!
# 退出
exit
```

- root 用户登录
- 新建 user lipingping 并登录
- lipingping 创建仓库
