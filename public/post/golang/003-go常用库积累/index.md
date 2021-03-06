
- [1：日志库](#1日志库)
- [2：配置库](#2配置库)
- [3：存储相关](#3存储相关)
- [4：数据结构](#4数据结构)
- [5：CLI 命令行](#5cli-命令行)
- [6：web 框架](#6web-框架)
- [7：RPC 和微服务](#7rpc-和微服务)
  - [7.1 Remote Procedure Call](#71-remote-procedure-call)
    - [7.1.1 原生 RPC](#711-原生-rpc)
    - [7.1.2 GRPC](#712-grpc)
      - [7.1.2.1 GRPC 安装](#7121-grpc-安装)
      - [7.1.2.2 GRPC 使用](#7122-grpc-使用)
      - [7.1.2.3 GRPC 测试](#7123-grpc-测试)
      - [7.1.2.4 GRPC 压测 ghz](#7124-grpc-压测-ghz)
  - [7.2 Micro Services](#72-micro-services)
- [8：标准库好用可替换库](#8标准库好用可替换库)
- [9：数据库相关](#9数据库相关)
- [10：MQ 库](#10mq-库)
- [11：微服务组件库](#11微服务组件库)
  - [11.1 限流](#111-限流)
  - [11.2 熔断](#112-熔断)
  - [11.3 链路追踪](#113-链路追踪)
- [12: 测试相关 related](#12-测试相关-related)
  - [12.1 单元测试](#121-单元测试)
  - [12.2 性能测试](#122-性能测试)
  - [12.3 FuzzTesting](#123-fuzztesting)
- [14: 性能分析](#14-性能分析)
  - [14.1 prof](#141-prof)
  - [14.2 trace](#142-trace)
- [13: 代码检测 related](#13-代码检测-related)
  - [13.1 竞态检测](#131-竞态检测)
  - [13.2 go vet 静态检查](#132-go-vet-静态检查)
  - [13.3 Shadowing variable](#133-shadowing-variable)
- [15: Others](#15-others)
  - [15.1 email 电子邮件](#151-email-电子邮件)
  - [15.2 热编译](#152-热编译)
  - [15.3 参数校验](#153-参数校验)
  - [15.4 任务调度工具](#154-任务调度工具)
  - [15.5 自动化运维平台](#155-自动化运维平台)
  - [15.6 deep preety print](#156-deep-preety-print)

# 1：日志库

```go
https://github.com/uber-go/zap
https://github.com/rs/zerolog
https://github.com/Sirupsen/logrus


// 日志滚动包
https://github.com/natefinch/lumberjack
```

# 2：配置库

```go
兼容 json，toml，yaml，hcl 等格式的日志库.
https://github.com/spf13/viper
```

# 3：存储相关

```go
mysql: https://github.com/go-xorm/xorm
es: https://github.com/elastic/elasticsearch
redis: https://github.com/gomodule/redigo
mongo: https://github.com/mongodb/mongo-go-driver
kafka: https://github.com/Shopify/sarama
```

# 4：数据结构

```go
https://github.com/emirpasic/gods
```

# 5：CLI 命令行

```go
https://github.com/spf13/cobra
```

# 6：web 框架

```go
// gin
// echo
// beego
// goframe
// firber

gocondor [A golang framework for building modern APIs]
// https://github.com/gocondor/gocondor
...
```

# 7：RPC 和微服务

```go
// grpc
https://github.com/grpc/grpc-go

// micro

```

## 7.1 Remote Procedure Call

### 7.1.1 原生 RPC

### 7.1.2 GRPC

#### 7.1.2.1 GRPC 安装

#### 7.1.2.2 GRPC 使用

#### 7.1.2.3 GRPC 测试

- **(1): [BloomRPC](https://github.com/uw-labs/bloomrpc)**

  - <1> **二进制安装**[https://github.com/uw-labs/bloomrpc/releases]
  - <2> **Source Code 安装**

  ```bash
  git clone https://github.com/uw-labs/bloomrpc.git
  cd bloomrpc

  yarn install && ./node_modules/.bin/electron-rebuild
  npm run package
  ```

- **(2): [grpcUI](https://github.com/fullstorydev/grpcui/)**

  - https://github.com/fullstorydev/grpcui/

  ```go
  // 安装
  go get github.com/fullstorydev/grpcui/...
  go install github.com/fullstorydev/grpcui/cmd/grpcui

  grpcui -help

  // 使用
  grpcui -plaintext localhost:12345
  gRPC Web UI available at http://127.0.0.1:60551/...

  // 错误
  Failed to compute set of methods to expose: server does not support the reflection API
  这种情况下，加个反射就可以了，在 listen 的 main.go 新增如下代码即可：`reflection.Register(s)`


  ```

#### 7.1.2.4 GRPC 压测 ghz

- https://ghz.sh/

```go
  ghz -insecure \
  --proto ./protos/routeguide.proto \
  --call routeguide.RouteGuide.GetFeature \
  --skipTLS \
  --insecure \
  -d '{"latitude":409146138,"longitude":-746188906}' \
  -c 100 \
  -n 100000 \
  localhost:50051

```

## 7.2 Micro Services

# 8：标准库好用可替换库

```go
// json
// map
// go pool
```

# 9：数据库相关

```go

```

# 10：MQ 库

```go

```

# 11：微服务组件库

## 11.1 限流

```go
https://github.com/uber-go/ratelimit
https://blog.csdn.net/chenchongg/article/details/85342086
https://github.com/juju/ratelimit
```

## 11.2 熔断

## 11.3 链路追踪

https://studygolang.com/articles/23528?fr=sidebar

# 12: 测试相关 related

## 12.1 单元测试

## 12.2 性能测试

## 12.3 FuzzTesting

# 14: 性能分析

## 14.1 prof

## 14.2 trace

# 13: 代码检测 related

## 13.1 竞态检测

`go run -race xxx.go `

## 13.2 go vet 静态检查

```go
go vet //只在一个单独的包内可用，不能使用flag 选项
go tool vet <directory|files> //更加完整，它可用用于文件和目录。目录被递归遍历来找到
```

## 13.3 Shadowing variable

- `也叫幽灵变量，影子变量`

- 不小心覆盖的变量
  对从动态语言转过来的开发者来说，简短声明很好用，这可能会让人误会 := 是一个赋值操作符。

如果你在新的代码块中像下边这样误用了 :=，编译不会报错，但是变量不会按你的预期工作：

```go
func main() {
    x := 1
    println(x)      // 1
    {
        println(x)  // 1
        x := 2
        println(x)  // 2    // 新的 x 变量的作用域只在代码块内部
    }
    println(x)      // 1
}
```

这是 Go 开发者常犯的错，而且不易被发现。

可使用官方提供的 vet 工具来诊断这种变量覆盖，它默认是不会自动执行的：

```go
> go tool vet -shadow main.go
main.go:9: declaration of "x" shadows declaration at main.go:5
```

但是官方的 vet 不会报告全部被覆盖的变量，这时候我们就要借助第三方包 —— **`go-nyet`** 来做进一步的检测了。

- **go-nyet**

```go
// go get
go get github.com/barakmich/go-nyet

// run
go-nyet ./...
# or
go-nyet subpackage
# or
go-nyet file.go

```

# 15: Others

## 15.1 email 电子邮件

```go
//
https://github.com/AfterShip/email-verifier

```

## 15.2 热编译

```go
gowatch
// https://github.com/silenceper/gowatch
// 配置文件示例:https://github.com/silenceper/gowatch/blob/master/example/gowatch.yml


air
// https://github.com/cosmtrek/air
// 配置文件示例:https://github.com/cosmtrek/air/blob/master/air_example.toml

```

## 15.3 参数校验

```go
validator
// https://github.com/go-playground/validator
```

## 15.4 任务调度工具

```go
cronsun
// https://github.com/shunfei/cronsun

gocron
// https://github.com/ouqiang/gocron

// cron 定时任务
https://github.com/robfig/cron
```

## 15.5 自动化运维平台

```go
gaia
// https://github.com/gaia-pipeline/gaia
```

## 15.6 deep preety print

```go
go-spew
// https://github.com/davecgh/go-spew
```
