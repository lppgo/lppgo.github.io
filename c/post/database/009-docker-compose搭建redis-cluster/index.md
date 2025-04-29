
<div align="center"><font size="35">docker-compose搭建redis cluster</font></div>

- [一: Redis Cluster 集群](#一-redis-cluster-集群)
- [二: 主从复制模式](#二-主从复制模式)
- [三: 哨兵模式](#三-哨兵模式)
- [三: Cluster 模式](#三-cluster-模式)
  - [3.1 `redis.conf`](#31-redisconf)
  - [3.2 目录结构](#32-目录结构)
  - [3.3 docker-compose 编排文件](#33-docker-compose-编排文件)
  - [3.4 测试 Redis 集群](#34-测试-redis-集群)
  - [3.5 Redis 集群 查看信息](#35-redis-集群-查看信息)
  - [3.6 Redis 集群 写入数据测试](#36-redis-集群-写入数据测试)
  - [3.7 redis 集群灾难测试](#37-redis-集群灾难测试)

# 一: Redis Cluster 集群

- 在 Redis 中，集群的解决方案有三种
  - 1.主从复制
  - 2.哨兵机制
  - 3.Cluster

# 二: 主从复制模式

Redis 虽然读取写入的速度都特别快，但是也会产生读压力特别大的情况。为了分担读压力，Redis 支持主从复制，读写分离。一个 Master 可以有多个 Slaves。
![redis-master-slave复制模式](/images/redis-master-slave复制模式.png)

- **优点**

  - 数据备份
  - 读写分离，提高服务器性能

- **缺点**
  - 不能自动故障恢复,RedisHA 系统（需要开发）
  - 无法实现动态扩容

# 三: 哨兵模式

Redis Sentinel 是社区版本推出的原生高可用解决方案，其部署架构主要包括两部分：Redis Sentinel 集群和 Redis 数据集群。

其中 Redis Sentinel 集群是由若干 Sentinel 节点组成的分布式集群，可以实现故障发现、故障自动转移、配置中心和客户端通知。Redis Sentinel 的节点数量要满足 2n+1（n>=1）的奇数个。
![哨兵模式](/images/redis-哨兵模式.png)

- **优点**

  - 1.自动化故障恢复

- **缺点**
  - 1.Redis 数据节点中 slave 节点作为备份节点不提供服务
  - 2.无法实现动态扩容

# 三: Cluster 模式

- Redis Cluster 是社区版推出的 Redis 分布式集群解决方案，主要解决 Redis 分布式方面的需求，比如，当遇到单机内存，并发和流量等瓶颈的时候，Redis Cluster 能起到很好的负载均衡的目的。

- Redis Cluster 着眼于提高并发量。

- 群集至少需要 3 主 3 从，且每个实例使用不同的配置文件。

- 在 redis-cluster 架构中，redis-master 节点一般用于接收读写，而 redis-slave 节点则一般只用于备份， 其与对应的 master 拥有相同的 slot 集合，若某个 redis-master 意外失效，则再将其对应的 slave 进行升级为临时 redis-master。

- 在 redis 的官方文档中，对 redis-cluster 架构上，有这样的说明：在 cluster 架构下，默认的，一般 redis-master 用于接收读写，而 redis-slave 则用于备份，当有请求是在向 slave 发起时，会直接重定向到对应 key 所在的 master 来处理。但如果不介意读取的是 redis-cluster 中有可能过期的数据并且对写请求不感兴趣时，则亦可通过 readonly 命令，将 slave 设置成可读，然后通过 slave 获取相关的 key，达到读写分离。具体可以参阅 redis 官方文档等相关内容
  ![Redis-Cluster](/images/redis-cluster-mode.png)

- **优点**

  - 1.解决分布式负载均衡的问题。具体解决方案是分片/虚拟槽 slot。
  - 2.可实现动态扩容
  - 3.P2P 模式，无中心化

- **缺点**
  - 1.为了性能提升，客户端需要缓存路由表信息
  - 2.Slave 在集群中充当“冷备”，不能缓解读压力

下面通过 docker-compose 搭建 redis cluster 集群

目录结构 端口(9001-9006) conf redis.conf data

## 3.1 `redis.conf`

```bash
# 端口
port 9001
# 密码
requirepass 123456
# Master节点密码
masterauth 123456
# 关闭保护模式
protected-mode no
# 开启集群
cluster-enabled yes
# 集群节点配置
cluster-config-file nodes.conf
# 超时
cluster-node-timeout 5000
# 集群节点IP host模式为宿主机IP
cluster-announce-ip 你自己的ip
# 集群节点端口 9001 - 9006
cluster-announce-port 9001
cluster-announce-bus-port 19001
# 开启 appendonly 备份模式
appendonly yes
# 每秒钟备份
appendfsync everysec
# aof文件进行压缩时，是否执行同步操作
no-appendfsync-on-rewrite no
# 当aof文件大小超过上一次重写时的aof文件大小的100%时会再次进行重写
auto-aof-rewrite-percentage 100
# 重写前AOF文件的大小最小值 默认 64mb
auto-aof-rewrite-min-size 64mb

# 日志配置
# debug:打印信息会很多，混乱的感觉。（开发/测试阶段）
# verbose:比debug级别好一点，仍然有很多不必要的信息。
# notice:于生产环境使用。
# warning:记录关键的警告消息。
loglevel notice
# 日志文件路径
logfile "/data/redis.log"
```

## 3.2 目录结构

9001 - 9006 每个目录格式如下:
![](/images/redis-目录结构.png)

## 3.3 docker-compose 编排文件

```yaml
version: "3.7"

services:
  redis9001:
    image: redis:6
    container_name: redis9001
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    volumes:
      - ./9001/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - ./9001/data:/data
    ports:
      - "9001:9001"
      - "19001:19001"
    environment:
      # 设置时区为上海，否则时间会有问题
      - TZ=Asia/Shanghai
    logging:
      options:
        max-size: "100m"
        max-file: "10"

  redis9002:
    image: redis:6
    container_name: redis9002
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    volumes:
      - ./9002/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - ./9002/data:/data
    ports:
      - "9002:9002"
      - "19002:19002"
    environment:
      # 设置时区为上海，否则时间会有问题
      - TZ=Asia/Shanghai
    logging:
      options:
        max-size: "100m"
        max-file: "10"

  redis9003:
    image: redis:6
    container_name: redis9003
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    volumes:
      - ./9003/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - ./9003/data:/data
    ports:
      - "9003:9003"
      - "19003:19003"
    environment:
      # 设置时区为上海，否则时间会有问题
      - TZ=Asia/Shanghai
    logging:
      options:
        max-size: "100m"
        max-file: "10"

  redis9004:
    image: redis:6
    container_name: redis9004
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    volumes:
      - ./9004/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - ./9004/data:/data
    ports:
      - "9004:9004"
      - "19004:19004"
    environment:
      # 设置时区为上海，否则时间会有问题
      - TZ=Asia/Shanghai
    logging:
      options:
        max-size: "100m"
        max-file: "10"

  redis9005:
    image: redis:6
    container_name: redis9005
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    volumes:
      - ./9005/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - ./9005/data:/data
    ports:
      - "9005:9005"
      - "19005:19005"
    environment:
      # 设置时区为上海，否则时间会有问题
      - TZ=Asia/Shanghai
    logging:
      options:
        max-size: "100m"
        max-file: "10"

  redis9006:
    image: redis:6
    container_name: redis9006
    command: ["redis-server", "/usr/local/etc/redis/redis.conf"]
    volumes:
      - ./9006/conf/redis.conf:/usr/local/etc/redis/redis.conf
      - ./9006/data:/data
    ports:
      - "9006:9006"
      - "19006:19006"
    environment:
      # 设置时区为上海，否则时间会有问题
      - TZ=Asia/Shanghai
    logging:
      options:
        max-size: "100m"
        max-file: "10"

networks:
  app_net:
    external: true
```

## 3.4 测试 Redis 集群

- ping 本机:`docker exec -it redis9001 /bin/sh redis-cli -h 192.168.0.100 -p 9001 -a 123456 ping`
- ping 其他机器:`redis-cli -h 192.168.0.100 -p 9005 -a 123456 ping`

## 3.5 Redis 集群 查看信息

- **查看集群信息** :`cluster info`
- **查看集群节点信息**: `cluster nodes`
- **查看集群 slots 分片**: `cluster slots`

## 3.6 Redis 集群 写入数据测试

```bash
set key1 value1;

```

## 3.7 redis 集群灾难测试

```go
docker stop redis9002
```
