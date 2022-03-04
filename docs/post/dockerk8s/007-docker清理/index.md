
- [Docker 清理常用方法](#docker-清理常用方法)
  - [1：Docker 积累的东西](#1docker-积累的东西)
  - [2：使用 docker 清理](#2使用-docker-清理)
    - [2.1：docker system](#21docker-system)
    - [2.1: 清理已经停止的容器](#21-清理已经停止的容器)
    - [2.2: 清理磁盘卷](#22-清理磁盘卷)
    - [2.3: 清理镜像](#23-清理镜像)
    - [2.4: 清理网络](#24-清理网络)
    - [2.5: 使用 docker-compose 清理](#25-使用-docker-compose-清理)
    - [2.6: docker system prune](#26docker-system-prune)

# Docker 清理常用方法

Docker 基于 Linux 内核通过操作系统和虚拟容器调用 CGroup, Namespace 等系统接口完成资源的分配与相互隔离，依赖系统资源运行，在分配回收过程中会产生一些垃圾，比如 docker stop 容器后没有执行 docker rm 删除。

## 1：Docker 积累的东西

你需要注意这些：

- 已经停止的容器
- 磁盘卷
- 镜像
- 网络

如果有足够的空间，你可能不太关心磁盘空间，但是网络也很重要。默认地，Docker 使用 bridge 网络，它的极限是 31 个网络。当达到极限时，你会看到下面这条消息：

```go
could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network
```

如果你是一个为每个项目创建一个网络的 docker-compose 重度用户，就会发生这种情况。你可以通过设置一个自定义--subnet 子网来解决问题，例如：

```go
docker network create dada --subnet 192.167.11.0/24
```

## 2：使用 docker 清理

### 2.1：docker system

**docker system df** 命令，类似于 Linux 上的 df 命令，用于查看 Docker 的磁盘使用情况：

```go
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          10        6         2.254GB   1.394GB (61%)
Containers      8         8         384.1MB   0B (0%)
Local Volumes   3         1         378.4kB   378.4kB (100%)
Build Cache     4         0         448B      448B
```

**docker system prune** 命令可以用于清理磁盘，删除关闭的容器、无用的数据卷和网络，以及 dangling 镜像（即无 tag 的镜像）。docker system prune -a 命令清理得更加彻底，可以将没有容器使用 Docker 镜像都删掉。注意，这两个命令会把你暂时关闭的容器，以及暂时没有用到的 Docker 镜像都删掉了……所以使用之前一定要想清楚吶。

### 2.1: 清理已经停止的容器

```go
docker rm -v $(docker ps --all --quiet --filter 'status=exited')
```

这会找到所有处于已退出（exited）状态的容器，一行一个地输出它们的 ID，以便我们可以将它提供给其它 shell 指令。

我们使用 docker rm -v 来删除任何匿名卷（没有显式名称的卷）。

### 2.2: 清理磁盘卷

上面的命令应该删除与该容器关联的卷。如果你手动创建卷，并要删除任何未被使用的卷：

```go
docker volume rm $(docker volume ls --quiet --filter 'dangling=true')
```

### 2.3: 清理镜像

通常删除所有 Docker 镜像是安全的。我们可以在需要的时候按需获取。通常在一个镜像被清理后，构建时间会更长，因为 docker 守护进程需要花时间再次下载镜像

```go
docker rm $(docker images --quiet)
docker rm --force $(docker images --quiet)
```

### 2.4: 清理网络

这很简单。我们可以删除任何网络，它会在之后按需重建。

```go
docker network rm $(docker network ls --quiet)
```

### 2.5: 使用 docker-compose 清理

如果你使用 docker-compose 启动容器，我们有一种简单的方法来清理与特定 compose 文件关联的资源。

```go
docker-compose down --volumes --rmi all --remove-orphans

// 这个命令不会删除匿名卷，因此你必须处理这些匿名卷。
```

### 2.6: docker system prune
