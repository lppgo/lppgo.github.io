
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
- [8：好用可替换库](#8好用可替换库)
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
  - [13.4 errcheck](#134-errcheck)
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
  - [16.21 go 加解密](#1621-go-加解密)
- [17 一些特殊的库 Lib](#17-一些特殊的库-lib)
- [18 tools 工具库](#18-tools-工具库)
- [19 金融交易相关](#19-金融交易相关)
- [20 gosdk](#20-gosdk)
  - [20.1 微信](#201-微信)
  - [20.2 钉钉](#202-钉钉)
- [21 go devops](#21-go-devops)
- [22 数据分析](#22-数据分析)

# 1：日志库

```go
https://github.com/hunterhug/golog

https://github.com/uber-go/zap
https://github.com/rs/zerolog
https://github.com/Sirupsen/logrus


// 日志滚动包
https://github.com/natefinch/lumberjack


// 日志分析和查询平台
https://github.com/clickvisual/clickvisual
```

# 2：配置库

```go
// viper 兼容 json，toml，yaml，hcl 等格式的配置库.
https://github.com/spf13/viper

// configor Golang Configuration tool that support YAML, JSON, TOML, Shell Environment
https://github.com/jinzhu/configor



// env
https://github.com/caarlos0/env

// Support for JSON, TOML, YAML, env, command line, file, S3 etc. Alternative to viper.
https://github.com/knadh/koanf

// A dead simple configuration manager for Go applications.
https://github.com/tucnak/store
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
https://github.com/emirpasic/gods (go数据结构，sets,lists,stacks,maps.trees,queues ...)

// mapstructure
https://github.com/mitchellh/mapstructure (map和struct转换)


// json
https://github.com/liu-cn/json-filter

// 延迟队列(delay queue)
github.com/morikuni/go-dqueue

// 无锁队列
https://github.com/lppgo/go-lockfree-queue


// map
https://github.com/cornelk/hashmap (线程安全,lockfree hashmap)
https://github.com/alphadose/haxmap (Fastest and most memory efficient golang concurrent hashmap)
https://github.com/orcaman/concurrent-map


// xmap
```

# 5：CLI 命令行

```go
https://github.com/spf13/cobra
https://github.com/urfave/cli/
```

# 6：web 框架

```go
// gin
https://github.com/JGLTechnologies/gin-rate-limit
https://github.com/appleboy/gin-jwt
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

//
https://github.com/air-go/rpc
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

- [Go gRPC Middleware](https://github.com/grpc-ecosystem/go-grpc-middleware):提供了拦截器的 interceptor 链式的功能，可以将多个拦截器组合成一个拦截器链，当然它还提供了其它的功能，所以以 gRPC 中间件命名;
- [grpc-multi-interceptor](https://github.com/kazegusuri/grpc-multi-interceptor): 是另一个 interceptor 链式功能的库，也可以将单向的或者流式的拦截器组合;
- [grpc_auth](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/auth): 身份验证拦截器;
- [grpc_ctxtags](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tags): 为上下文增加 Tag map 对象;
- [grpc_zap](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/logging/zap): 支持 zap 日志框架;
- [grpc_logrus](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/logging/logrus): 支持 logrus 日志框架;
- [grpc_prometheus](https://github.com/grpc-ecosystem/go-grpc-prometheus): 支持 prometheus;
- [otgrpc](https://github.com/grpc-ecosystem/grpc-opentracing/tree/master/go/otgrpc): 支持 opentracing/zipkin;
- [grpc_opentracing](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing):支持 opentracing/zipkin;
- [grpc_retry](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/retry): 为客户端增加重试的功能;
- [grpc_validator](https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/validator): 为服务器端增加校验的功能

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

  - <https://github.com/fullstorydev/grpcui/>

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

  - [**`ptg`**](https://github.com/crossoverJie/ptg): 用 Go 写的 GUI gRPC 客户端

#### 7.1.2.5 GRPC 压测 ghz

- <https://ghz.sh/>

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

- <https://github.com/crossoverjie/ptg>

## 7.2 Micro Services

# 8：好用可替换库

- <https://github.com/nikgalushko/fx>

```go
// json
https://github.com/bytedance/sonic

// map

// go pool
https://gitee.com/xuesongtao/taskpool/tree/master
ants
https://github.com/sourcegraph/conc // Better structured concurrency for go

// map
https://github.com/heiyeluren/xmm

//
https://github.com/sasha-s/go-deadlock

// websocket
https://pkg.go.dev/github.com/gorilla/websocket
https://github.com/lxzan/gws

// channel
https://github.com/bruceshao/lockfree  比原生channel更快的lockfree队列
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


// mongo
https://github.com/qiniu/qmgo

```

# 10：MQ 库

```go

```

# 11：微服务组件库

- <https://github.com/go-micro-dev/plugins>

## 11.1 限流

```go
https://github.com/uber-go/ratelimit
https://blog.csdn.net/chenchongg/article/details/85342086
https://github.com/juju/ratelimit
https://github.com/JGLTechnologies/gin-rate-limit

// 分布式速率限制的滑动窗口算法的 Golang 实现
https://github.com/RussellLuo/slidingwindow

// 分布式应用程序的 Golang 速率限制器
https://github.com/mennanov/limiters

// throttled 基于通用信元速率算法实现了对资源的访问速率限制，资源可以是特定的 URL、用户或者任何自定义的形式，可以很方便地与各种 http 和 rpc 框架进行集成。throttled 定义了限流元信息的存储抽象，并内置了 memstore，redis store 等元信息存储实现，我们可以根据具体的使用场景实现单机限流和集群限流
https://github.com/throttled/throttled


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

- <https://studygolang.com/articles/23528?fr=sidebar>
- <https://github.com/go-micro-dev/plugins/blob/master/wrapper/trace/opentracing/opentracing.go>
- <https://github.com/lppgo/my_test/tree/master/040_opentracing>
- <https://github.com/uptrace/uptrace>
- <https://github.com/uptrace/uptrace-go>
- <https://github.com/Kashoo/go-micro-opentelemetry>

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

- **ThreadLocal for Golang** :<https://github.com/timandy/routine>

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

// 依赖分析
https://github.com/loov/goda

// Visualize Go Dependency Trees
https://github.com/KyleBanks/depth

// 以Graphviz 点格式展示依赖图
github.com/kisielk/godepgraph
godepgraph -s import-cycle-example | dot -Tpng -o godepgraph.png
```

# 13: 代码检测 related

## 13.1 竞态检测

`go run -race xxx.go`

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

## 13.4 errcheck

- `https://github.com/kisielk/errcheck` 用来检查未处理的 error

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
https://github.com/deatil/doak-cron

// coming 是一个原生的任务调度系统，目前给出了定时任务和计划任务的解决方案
https://github.com/alexanyang/coming
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

// decimal
https://github.com/shopspring/decimal

// gonum
https://github.com/gonum/gonum
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

## 16.21 go 加解密

```go
https://github.com/golang-module/dongle
https://github.com/lppgo/my_test/tree/master/033_%E5%8A%A0%E8%A7%A3%E5%AF%86
https://github.com/deatil/go-cryptobin
```

# 17 一些特殊的库 Lib

- 1. **端口复用**
     <https://github.com/libp2p/go-reuseport>
- 2. **自动调整 maxprocs**
     <https://github.com/uber-go/automaxprocs>
- 3. **auto adjust your GOGC value**
     <https://github.com/cch123/gogctuner>
- 4. **GeoIP2**
     <https://github.com/Hackl0us/GeoIP2-CN>

- 5. **汉字拼音**
     <https://github.com/mozillazg/go-pinyin>

- 6. **Go 语言给编译出来的程序添加图标和版本信息**
     <https://github.com/josephspurrier/goversioninfo>
     <https://studygolang.com/topics/15789>
- 7. **yaegi 是一个 go 语言解释器**
     <https://github.com/traefik/yaegi>
- 8. **golang 进度条展示**
     <https://github.com/qianlnk/pgbar>
- 9. **go+web 开发桌面应用**
     现代化 Web 技术开发桌面应用的 Go 框架
     <https://wails.io/docs/introduction>
- 10. **将 c 代码转成 go 代码**
      <https://gitlab.com/cznic/ccgo>

- 11. **将 proto 和 json 转换的库 protojson**
      Go 实现 Protocol Buffers 与 JSON 转换：protojson
      <https://juejin.cn/post/7281905382484672523>
      google.golang.org/protobuf/encoding/protojson

# 18 tools 工具库

- 1. **ztool**
     <https://github.com/druidcaesa/ztool>
     <https://studygolang.com/articles/35697#reply0>

- 2. **lancet** lancet（柳叶刀）是一个全面、高效、可复用的 go 语言工具函数库
     <https://github.com/duke-git/lancet>

# 19 金融交易相关

```go
// 期货期权 ctp 接口 Golang版 (for linux64)
https://gitee.com/mayiweb/goctp

// 股票期权 ctp 接口 Golang版 (for linux64)
https://gitee.com/mayiweb/goctp_sopt


// 恒生 股票期权 极速api 接口 Golang版 (for linux64)
https://gitee.com/mayiweb/gohs


//
https://github.com/krenx1983/openctp

// 处理货币与金融领域的库
https://github.com/jobbole/awesome-go-cn#%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86
accounting : Go语言金钱及货币格式  https://github.com/leekchan/accounting
currency : 处理货币金额,提供货币信息和格式。
currency : 高性能、精确的货币计算包。
decimal : 支持任意精度的十进制数的go包  https://github.com/shopspring/decimal
fastme : Go实现的 快速可扩展的匹配引擎 。
go-finance : Go中的综合金融市场数据。
go-finance : 用于货币时间价值（年金）、现金流、利率转换、债券和折旧计算的金融函数库。
go-finance : 用于获取汇率、通过VIES查询增值税号和查询IBAN银行账号的模块。
go-finnhub : 来自finnhub.io的股市、外汇和加密数据客户端。访问来自60多家证券交易所、10家外汇经纪商和15家以上加密交易所的实时金融市场数据。
go-money : Fowler's Money模式的实现。
ofxgo : 查询 OFX 服务器并解析其响应 (有一个示例的命令行客户端)
orderbook : Golang中的限价订单簿的匹配引擎。
techan : 具有高级市场分析和交易策略的技术分析库。
transaction : 以多线程模式运行的嵌入式的账户交易数据库,。
vat : VAT 验证及欧洲增值税率工具

```

# 20 gosdk

- sdk 三方库:<https://github.com/eryajf/third-tools>
- Go 开发常用工具库, Google2 步验证客户端,AES 加密解密,RSA 加密解密,钉钉机器人,邮件发送,JWT 生成解析,Log,BoltDB 操作,图片操作,json 操作,struct 序列化
  - <https://github.com/chanyipiaomiao/hltool>

## 20.1 微信

```go
// PowerWeChat是一款简单易用的WeChat SDK for Golang目前已经覆盖微信公众号、微信小程序、微信支付、企业微信。功能非常的强大，几乎是把微信生态的产品都包含在内
https://powerwechat.artisan-cloud.com/

// go-wechat-miniapp-sdk
https://github.com/dgb8901/go-wechat-miniapp-sdk

https://github.com/wenerme/go-wecom

// 利用企业微信像微信发信息
https://github.com/saucer-man/wepush

// 企业微信群机器人接口 Golang 封装
https://github.com/vimsucks/wxwork-bot-go
```

## 20.2 钉钉

```go
https://github.com/CatchZeng/dingtalk

https://github.com/zhaoyunxing92/dingtalk
```

# 21 go devops

```go
// ---------------- gitlab -------------------
// Gogs 是一款极易搭建的自助 Git 服务,类似gitlab
https://github.com/gogs/gogs/blob/main/README_ZH.md
// 女娲 - 开源 DevOps CI/CD 自动构建和自动部署系统
https://github.com/nvwa-io/nvwa-io


// ---------------- iptables -------------------
// iptables-web是一个轻量级的iptables web管理界面程序
https://github.com/pretty66/iptables-web


// Docker for YApi 一键部署YApi
https://github.com/jinfeijie/yapi

// Syncd - 自动化部署工具
https://github.com/dreamans/syncd

// Infinite 用于开发交互式 CLI(tui,terminal) 程序的组件库
https://fzdwx.github.io/infinite/


// mysql  审计平台
https://github.com/cookieY/Yearning

// supervisord
https://github.com/ochinchina/supervisord

// 可交互的网络探测分析器
https://github.com/chenjiandongx/sniffer

// 短链接
https://github.com/weiwei2012holy/short_url


// go流量回放
https://github.com/buger/goreplay

// 截图并发给robot
https://github.com/eryajf/care-screenshot

// 打印表格table
https://github.com/liushuochen/gotable


// prometheus 仪表盘instrumentation库
https://github.com/prometheus/client_golang


// Semaphore is a 运行 Ansible playbook 的响应式web UI
https://docs.ansible-semaphore.com/

// gossh
https://github.com/krilor/gossh

```

# 22 数据分析

- 类似于 numpay,pandas
- Go 中的数据分析——如何使用 `Gota` 包:<https://www.freecodecamp.org/news/exploratory-data-analysis-in-go-with-gota/>

- **feature**格式: `https://github.com/lppgo/feather`
- **dbf**格式:
  - `https://github.com/kcasctiv/dbf3`
  - `github.com/LindsayBradford/go-dbf v0.0.0-20181206104747-5f7a16f88561` // 注意版本
