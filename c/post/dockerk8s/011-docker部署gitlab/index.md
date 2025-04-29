
<div align="center"><font size="35">docker部署gitlab</font></div>

- [1：gitlab docker 镜像 pull](#1gitlab-docker-镜像-pull)
- [2：启动脚本](#2启动脚本)
- [3：修改`gitlab.rb`](#3修改gitlabrb)
- [4：修改 password](#4修改-password)

# 1：gitlab docker 镜像 pull

- `docker pull gitlab/gitlab-ce:latest`
- 新建目录`~/gitlab`

# 2：启动脚本

`~/gitlab/start.sh`

```bash
#!/bin/bash
GITLAB_DIR=/home/lucas/gitlab/data

docker run -d \
    -p 5443:443 \
    -p 9998:9998 \
    -p 2222:22 \
    --name gitlab \
    -v ${GITLAB_DIR}/config:/etc/gitlab \
    -v ${GITLAB_DIR}/logs:/var/log/gitlab \
    -v ${GITLAB_DIR}/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest
```

# 3：修改`gitlab.rb`

`~/gitlab/data/config/gitlab.rb`

```bash
# gitlab访问地址，可以写域名。如果端口不写的话默认为80端口
external_url 'http://0.0.0.0:9998'
# ssh主机ip
gitlab_rails['gitlab_ssh_host'] = '0.0.0.0'
# ssh连接端口
gitlab_rails['gitlab_shell_ssh_port'] = 22
```

# 4：修改 password

- docker exec -it gitlab 容器 ID bash

- 修改 pw

```bash
  gitlab-rails console -e production
  user = User.where(id: 1).first
  user.password = '12345678'
  user.password_confirmation = '12345678'
  user.save!
```
