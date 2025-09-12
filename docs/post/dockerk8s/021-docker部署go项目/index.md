
<div align="center"><font size="35">Docker部署go项目</font></div>

# 1: 准备 Go 项目

- 确保 Go 项目已经编写完成，并且可以在本地正常运行。
- 项目目录结构如下：

  ```
  ├── main.go
  ├── go.mod
  ├── go.sum
  ├── Dockerfile
  ├── Makefile
  ```

  - `main.go`：Go 项目的入口文件。
  - `go.mod`：Go 项目的依赖管理文件。
  - `go.sum`：Go 项目的依赖管理文件。
  - `Dockerfile`：Dockerfile 文件，用于构建 Docker 镜像。
  - `Makefile`：Makefile 文件，用于简化构建过程。

# 2: 编写 Dockerfile

## 2.1 基础镜像

- 在项目根目录下创建 `Dockerfile` 文件，内容如下：

  ```Dockerfile
  # 基础镜像
  FROM golang:1.19-alpine

  # 为我们的镜像设置必要的环境变量
  ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64 \
    GOPROXY=https://goproxy.cn,direct

  # 工作目录
  WORKDIR /app

  # 复制项目代码
  COPY . /app

  # 构建项目
  RUN go mod tidy && go build -o main .

  # 暴露端口
  EXPOSE 2080

  # 启动项目
  CMD ["/app/main"]
  ```

## 2.2 分阶段镜像

- 为了减小镜像大小，我们可以使用分阶段镜像。
- 分阶段镜像的思路是：先在一个阶段中构建项目，然后在另一个阶段中复制构建好的项目到最终的镜像中。
- 分阶段镜像的 Dockerfile 内容如下：

```Dockerfile
FROM golang:alpine AS builder
# 为我们的镜像设置必要的环境变量
ENV GO111MODULE=on \
CGO_ENABLED=0 \
GOOS=linux \
GOARCH=amd64 \
GOPROXY=https://goproxy.cn,direct
# 移动到工作目录：/build
WORKDIR /build
# 将代码复制到容器中
COPY . .
# 将我们的代码编译成二进制可执行文件
RUN go mod tidy && go build -o main .
# 移动到用于存放生成的二进制文件的 /dist 目录
WORKDIR /dist
# 将二进制文件从 /build 目录复制到这里
RUN cp /build/app .
## 声明服务端口
#EXPOSE 8989
### 启动容器时运行的命令
#CMD ["/dist/app"]

########################################
# 接下来创建一个小镜像
###################
FROM scratch
# 从builder镜像中把/dist/app 拷贝到当前目录
COPY --from=builder /build/app
/EXPOSE 8989
# 需要运行的命令
ENTRYPOINT ["/app"]
```

# 3: 构建镜像 image

- 在项目根目录下执行以下命令构建镜像：`docker build . -t web`
- 给 image 打标签：`docker tag web:latest web:v1`
- 查看镜像：`docker images`
- 导出 image：`docker save -o web.tar web:v1`
- 导入 image：`docker load -i web.tar`
- 上传到 私有镜像仓库：`docker push 172.31.1.40:5000/pfinalclub/web:v1`
- 从私有镜像仓库拉取镜像：`docker pull 172.31.1.40:5000/pfinalclub/web:v1`
- 私有化部署 docker 仓库：<https://yeasy.gitbook.io/docker_practice/repository/registry>

# 4: 运行 docker 容器

- 运行容器：`docker run -d -p 2080:2080 web:v1`
- 连接容器：`docker exec -it <container_id> /bin/sh`
- 查看容器：`docker ps`
- 查看日志：`docker logs -f <container_id>`
- 停止容器：`docker stop <container_id>`
- 删除容器：`docker rm <container_id>`
- 删除镜像：`docker rmi <image_id>`
- 查看镜像：`docker images`
- 查看容器端口映射：`docker port <container_id>`
- 查看容器 ip：`docker inspect <container_id> | grep IPAddress`
- 查看容器端口：`docker inspect <container_id> | grep Port`
- 查看容器环境变量：`docker inspect <container_id> | grep Env`
- 查看容器挂载卷：`docker inspect <container_id> | grep Mounts`
- 查看容器网络：`docker inspect <container_id> | grep NetworkSettings`
- 查看容器配置：`docker inspect <container_id>`
