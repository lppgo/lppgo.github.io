
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
      - [7.1.2.3 grpc-middleware](#7123-grpc-middleware)
      - [7.1.2.4 GRPC 测试](#7124-grpc-测试)
      - [7.1.2.5 GRPC 压测 ghz](#7125-grpc-压测-ghz)
  - [7.2 Micro Services](#72-micro-services)
- [8：标准库好用可替换库](#8标准库好用可替换库)
- [9：数据库相关](#9数据库相关)
- [10：MQ 库](#10mq-库)
- [11：微服务组件库](#11微服务组件库)
  - [11.1 限流](#111-限流)
  - [11.2 熔断 CircuitBreaker](#112-熔断-circuitbreaker)
  - [11.3 链路追踪](#113-链路追踪)
    - [11.3.1 openTracing](#1131-opentracing)
    - [11.3.2 oepnTelemetry](#1132-oepntelemetry)
- [12: 测试相关 related](#12-测试相关-related)
  - [12.1 单元测试](#121-单元测试)
  - [12.2 性能测试](#122-性能测试)
  - [12.3 FuzzTesting](#123-fuzztesting)
  - [12.4 LoadTesting](#124-loadtesting)
- [14: 性能分析](#14-性能分析)
  - [14.1 prof](#141-prof)
  - [14.2 trace](#142-trace)
  - [14.3 性能可视化分析](#143-性能可视化分析)
- [13: 代码检测 related](#13-代码检测-related)
  - [13.1 竞态检测](#131-竞态检测)
  - [13.2 go vet 静态检查](#132-go-vet-静态检查)
  - [13.3 Shadowing variable](#133-shadowing-variable)
- [15: health/status checking](#15-healthstatus-checking)
- [16: Others](#16-others)
  - [16.1 email 电子邮件](#161-email-电子邮件)
  - [16.2 热编译](#162-热编译)
  - [16.3 参数校验](#163-参数校验)
  - [16.4 任务调度工具](#164-任务调度工具)
  - [16.5 自动化运维平台](#165-自动化运维平台)
  - [16.6 deep preety print](#166-deep-preety-print)
  - [16.7 Juniper 是一个使用泛型扩展 Go 标准库的库，包括容器、迭代器和 stream](#167-juniper-是一个使用泛型扩展-go-标准库的库包括容器迭代器和-stream)
  - [16.8 samber/lo](#168-samberlo)
  - [16.9 gopsutil](#169-gopsutil)
  - [16.10 数学相关的库](#1610-数学相关的库)
  - [16.11 提供优化的算法以利用现代 CPU 的特性](#1611-提供优化的算法以利用现代-cpu-的特性)
  - [16.12 FTP](#1612-ftp)
  - [16.13 使用 cmux 实现服务端连接多路复用](#1613-使用-cmux-实现服务端连接多路复用)
  - [16.14 Golang 时间与日期](#1614-golang-时间与日期)
  - [16.15 Console progress bar 进度条](#1615-console-progress-bar-进度条)
  - [16.16 图表 chart](#1616-图表-chart)
  - [16.17 读写文件相关](#1617-读写文件相关)
  - [16.18 数学 math](#1618-数学-math)
  - [16.19 流量录制](#1619-流量录制)
  - [16.20 常用软件 SDK](#1620-常用软件-sdk)
    - [16.20.1 钉钉 dingtalk](#16201-钉钉-dingtalk)
    - [16.20.1 微信 wechat](#16201-微信-wechat)
- [17 一些特殊的库 Lib](#17-一些特殊的库-lib)
- [18 tools 工具库](#18-tools-工具库)

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
// viper 兼容 json，toml，yaml，hcl 等格式的配置库.
https://github.com/spf13/viper

// configor Golang Configuration tool that support YAML, JSON, TOML, Shell Environment
https://github.com/jinzhu/configor


// env
https://github.com/caarlos0/env
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
https://github.com/asim/go-micro

// kratos
https://go-kratos.dev/docs/getting-started/usage
```

## 7.1 Remote Procedure Call

### 7.1.1 原生 RPC

### 7.1.2 GRPC

#### 7.1.2.1 GRPC 安装

#### 7.1.2.2 GRPC 使用

#### 7.1.2.3 grpc-middleware

```go
https://github.com/grpc-ecosystem/go-grpc-middleware
```

#### 7.1.2.4 GRPC 测试

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

#### 7.1.2.5 GRPC 压测 ghz

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

- https://github.com/crossoverjie/ptg

## 7.2 Micro Services

# 8：标准库好用可替换库

```go
// json
https://github.com/bytedance/sonic
https://github.com/bytedance/sonic
// map
// go pool
https://gitee.com/xuesongtao/taskpool/tree/master
```

# 9：数据库相关

```go
// gorm

// db2gorm 根据数据库表生成对应的struct
https://github.com/qmhball/db2gorm
github.com/gohouse/converter

// gormt
https://gitee.com/mirrors/gormt

// table2struct
https://github.com/jiazhoulvke/table2struct

```

# 10：MQ 库

```go

```

# 11：微服务组件库

- https://github.com/go-micro-dev/plugins

## 11.1 限流

```go
https://github.com/uber-go/ratelimit
https://blog.csdn.net/chenchongg/article/details/85342086
https://github.com/juju/ratelimit

// 分布式速率限制的滑动窗口算法的 Golang 实现
https://github.com/RussellLuo/slidingwindow

// 分布式应用程序的 Golang 速率限制器
https://github.com/mennanov/limiters
```

## 11.2 熔断 CircuitBreaker

```go
// gobreaker
https://github.com/sony/gobreaker

// hystrix-go
https://github.com/afex/hystrix-go
```

## 11.3 链路追踪

### 11.3.1 openTracing

### 11.3.2 oepnTelemetry

- https://studygolang.com/articles/23528?fr=sidebar
- https://github.com/go-micro-dev/plugins/blob/master/wrapper/trace/opentracing/opentracing.go
- https://github.com/lppgo/my_test/tree/master/040_opentracing
- https://github.com/uptrace/uptrace
- https://github.com/uptrace/uptrace-go
- https://github.com/Kashoo/go-micro-opentelemetry

# 12: 测试相关 related

```go
https://github.com/kyoh86/richgo
```

## 12.1 单元测试

## 12.2 性能测试

## 12.3 FuzzTesting

## 12.4 LoadTesting

```go
fortio
// https://github.com/fortio/fortio
```

# 14: 性能分析

## 14.1 prof

## 14.2 trace

## 14.3 性能可视化分析

```go
// statsviz 即时实时可视化 Heap、Objects、Goroutines、GC 等
https://github.com/arl/statsviz
https://polarisxu.studygolang.com/posts/go/pkg/statsviz/

// statsview  一个实时的 Golang runtime stats visualization profiler
https://github.com/go-echarts/statsview

// parca 持续分析以分析 CPU、内存使用量随时间的变化，直至行号
https://github.com/parca-dev/parca

//
https://studygolang.com/topics/14979
https://github.com/xyctruth/profiler

// autopprof
https://github.com/lppgo/autopprof

//
https://github.com/loov/goda

//
https://github.com/KyleBanks/depth
```

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

# 15: health/status checking

- 服务健康状态检查

```go
// AlterManager


// easyprobe
https://github.com/megaease/easeprobe
```

# 16: Others

## 16.1 email 电子邮件

```go
//
https://github.com/AfterShip/email-verifier
https://github.com/jordan-wright/email

```

## 16.2 热编译

```go
gowatch
// https://github.com/silenceper/gowatch
// 配置文件示例:https://github.com/silenceper/gowatch/blob/master/example/gowatch.yml


air
// https://github.com/cosmtrek/air
// 配置文件示例:https://github.com/cosmtrek/air/blob/master/air_example.toml

```

## 16.3 参数校验

```go
validator
// https://github.com/go-playground/validator
```

## 16.4 任务调度工具

```go
cronsun
// https://github.com/shunfei/cronsun

gocron
// https://github.com/ouqiang/gocron

// cron 定时任务
https://github.com/robfig/cron
```

## 16.5 自动化运维平台

```go
gaia
// https://github.com/gaia-pipeline/gaia
```

## 16.6 deep preety print

```go
go-spew
// https://github.com/davecgh/go-spew
```

## 16.7 Juniper 是一个使用泛型扩展 Go 标准库的库，包括容器、迭代器和 stream

```go
juniper
// https://github.com/bradenaw/juniper
```

## 16.8 samber/lo

- Lodash 是一个内部封装了诸多对字符串、数组、对象等常见的数据类型的处理函数的一套工具库
- A Lodash-style Go library based on Go 1.18+ Generics (map, filter, contains, find...)

```go
lo
// https://github.com/samber/lo
```

## 16.9 gopsutil

- gopsutil psutil for golang

```go
https://github.com/shirou/gopsutil
https://mp.weixin.qq.com/s/yTblk9Js1Zcq5aWVcYGjOA
```

## 16.10 数学相关的库

```go
// 任意精度小数decimals
https://github.com/cockroachdb/apd

// 数学统计，中位数，平均值等
https://github.com/montanaflynn/stats
```

## 16.11 提供优化的算法以利用现代 CPU 的特性

```go
https://github.com/segmentio/asm
```

## 16.12 FTP

```go
// 基于 Golang 的自治 FTP 服务器，带有 SFTP、S3、Dropbox 和 Google Drive 连接器。
https://github.com/fclairamb/ftpserver
```

## 16.13 使用 cmux 实现服务端连接多路复用

```go
// cmux
https://mp.weixin.qq.com/s/2cERDCRKlmfHKv8gY324Hg
https://github.com/soheilhy/cmux
```

## 16.14 Golang 时间与日期

```go
// carbon 是一个轻量级、语义化、对开发者友好的golang时间处理库，支持链式调用
https://github.com/golang-module/carbon

https://github.com/jinzhu/now
```

## 16.15 Console progress bar 进度条

```go
// Console progress bar for Golang
https://github.com/cheggaaa/pb

//
https://github.com/schollz/progressbar
```

## 16.16 图表 chart

```go
https://github.com/go-echarts/go-echarts
```

## 16.17 读写文件相关

```go
// excelize


// cvs
```

## 16.18 数学 math

```go
// decimal
https://github.com/shopspring/decimal
```

## 16.19 流量录制

```go
https://github.com/didi/sharingan
```

## 16.20 常用软件 SDK

### 16.20.1 钉钉 dingtalk

```go
https://github.com/zhaoyunxing92/dingtalk
```

### 16.20.1 微信 wechat

```go

```

# 17 一些特殊的库 Lib

```go
// 端口复用
https://github.com/libp2p/go-reuseport
// 自动调整maxprocs
https://github.com/uber-go/automaxprocs
// auto adjust your GOGC value
https://github.com/cch123/gogctuner
```

# 18 tools 工具库

```go
// ztool
https://github.com/druidcaesa/ztool
https://studygolang.com/articles/35697#reply0


```
