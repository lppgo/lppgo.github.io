
- [1: 安装 gitlab](#1-安装-gitlab)
  - [1.1 安装](#11-安装)
  - [1.2 配置](#12-配置)
  - [1.3 启动 gitlab](#13-启动-gitlab)
  - [1.4 account 管理](#14-account-管理)
- [2: 内网穿透 natapp](#2-内网穿透-natapp)

# 1: 安装 gitlab

## 1.1 安装

- https://packages.gitlab.com/gitlab/gitlab-ce/install
- 安装工具包: `apt install  policycoreutils-python-utils`
- 安装 gitlab: `curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash`
- `sudo apt install gitlab-ce`

- 安装成功成功出现如下图所示:
  ![](/images/gitlab_001.png)

## 1.2 配置

- 更新配置 :`gitlab-ctl reconfigure`。装完成后,更新配置,稍微需要点时间,耐心等待一下,完成后,我们可以看到用户名和密码
- 以下信息我们可以看到用户名和密码,用户名为:root,密码需要单独查看
  ![](/images/gitlab_002.png)
- 上面那个路径就是密码路径,查看密码:`cat /etc/gitlab/initial_root_password`

## 1.3 启动 gitlab

- `gitlab-ctl start`;

- 然后修改访问地址,编辑 Gitlab 配置文件: `vim /etc/gitlab/gitlab.rb`;把 external_url 的值换成http://127.0.0.1:8088,端口号可以自己指定,这里指定8088,然后保存;
- 修改完后重新加载配置文件: `gitlab-ctl reconfigure`;配置生效可能需要 1 分钟左右。
- 然后重新启动 Gitlab: `sudo gitlab-ctl restart`;
- 如果有防火墙,添加防火墙端口:8088: `firewall-cmd --zone=public --add-port=8088/tcp --permanent`;
- 然后打开浏览器,输入 Linux 局域网 ip+8088,即可访问成功:
  ![](/images/gitlab_003.png)
- 输入上面的用户名:root 和上面查看的密码即可登录成功啦;

## 1.4 account 管理

- root 默认密码修改.
- 新增注册 account，并使用管理员批准;
- 创建仓库并使用 gitlab;

# 2: 内网穿透 natapp

- 申请隧道并配置:https://natapp.cn/tunnel/lists
- 配置并启动 natapp: `./natapp --config=config.ini`;
- config.ini

```ini
[default]
authtoken=d6cfbd7e1855ca3b
```

- 配置

```go
Version                 2.3.9                                                           │Version                 2.3.9
                                                                                        │
Forwarding              tcp://server.natappfree.cc:46828 -> 127.0.0.1:22                │Forwarding              http://s7nakp.natappfree.cc -> 127.0.0.1:9989
                                                                                        │
Web Interface           http://127.0.0.1:4040                                           │Web Interface           http://127.0.0.1:4040
                                                                                        │
Total Connections       2                                                               │Total Connections       0
```
