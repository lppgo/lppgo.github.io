
# Table of Contents

- [Table of Contents](#table-of-contents)
- [1：开发工具](#1开发工具)
- [2：调试工具](#2调试工具)
- [3：常用网站](#3常用网站)
- [4：golang 常用库](#4golang-常用库)

# 1：开发工具

> 1: **sql2go** sql 语句转换为 Go 结构体，使用 ddl。
> http://stming.cn/tool/sql2go.html

> 2: **json2go** 将 json 格式转为 Go struct
> https://mholt.github.io/json-to-go/

> 3: **toml2go** 将编码后的 toml 文本转为 Go struct
> https://xuri.me/toml-to-go/

> 4: **curl2go** 将 curl 命令转为 go 代码
> https://mholt.github.io/curl-to-go/

> 5: **mysql 转 ES** sql 语句转换为 ES 语句。
> http://www.ischoolbar.com/EsParser/

> 6: **go 压缩解压库** 一个好用的文件压缩和解压工具，集成了 zip，tar 等多种功能，主要还有跨平台。
> https://github.com/mholt/archiver

> 7: **go list / go vet** 查看某一个包的依赖关系，检查代码中不符合 golang 规范的地方。
> https://pkg.go.dev/cmd/go

> 8: **热编译工具** 本地开发调试时很方便，修改代码后自动重启。
> https://github.com/silenceper/gowatch

> 9: **revive** golang 代码质量检测工具
> https://github.com/mgechev/revive

> 10: **Go Callvis** golang 的代码调用链图工具
> https://github.com/ofabry/go-callvis

> 11: **Realize / Air** Go 本地开发常用的实时重载工具。
> https://github.com/oxequa/realize > https://github.com/cosmtrek/air

> 12: **gotests** 自动生成测试用例工具
> https://github.com/cweill/gotests

> 13: **gomodifytags** Go tool to modify struct field tags
> https://github.com/fatih/gomodifytags

# 2：调试工具

> 1: **perf**
> 代理工具，支持内存，cpu，堆栈查看，并支持火焰图。
> perf 工具和 go-torch 工具，快捷定位程序问题。
> https://github.com/uber-archive/go-torch > https://github.com/google/gops

> 2: **dlv 远程调试**
> 基于 goland+dlv 可以实现远程调试的能力。
> https://github.com/go-delve/delve
> 提供了对 golang 原生的支持，相比 gdb 调试，简单太多。

> 3: **网络代理工具**
> goproxy 代理，支持多种协议，支持 ssh 穿透和 kcp 协议。
> https://github.com/snail007/goproxy

> 4: **抓包工具**
> go-sniffer 工具，可扩展的抓包工具，可以开发自定义协议的工具包。
> 现在只支持了 http，mysql，redis，mongodb。
> https://github.com/40t/go-sniffer

> 5: **反向代理工具 ngrok**，快捷开放内网端口供外部使用。
> ngrok 可以让内网服务外部调用
> https://ngrok.com/ > https://github.com/inconshreveable/ngrok

> 6: **配置化生成证书**
> 从根证书，到业务侧证书一键生成。
> https://github.com/cloudflare/cfssl

> 7: **免费的证书获取工具**
> 基于 acme 协议，从 letsencrypt 生成免费的证书，可自动续期。
> https://github.com/acmesh-official/acme.sh

> 8: **开发环境管理工具 vagrant**，单机搭建可移植工具的利器。支持多种虚拟机后端。
> https://github.com/hashicorp/vagrant

> 9: **轻量级容器调度工具 nomad**
> nomad 可以非常方便的管理容器和传统应用，相比 k8s 来说简单不少。
> https://github.com/hashicorp/nomad

> 10: **高度可配置化的 http 转发工具**，基于 etcd 配置。
> https://github.com/gojek/weaver

> 11: **进程监控工具 supervisor**
> https://www.jianshu.com/p/39b476e808d8

> 12: **基于 procFile 进程管理工具**，相比 supervisor 更加简单。
> https://github.com/ddollar/foreman

> 13: **基于 http，https，websocket 的调试代理工具**，配置功能丰富。
> https://github.com/avwo/whistle

> 14: **分布式调度工具**
> https://github.com/shunfei/cronsun/blob/master/README_ZH.md > https://github.com/ouqiang/gocron

> 15: **自动化运维平台 Gaia**
> https://github.com/gaia-pipeline/gaia

# 3：常用网站

> 1: **pkg.go.dev** 官方包文档和第三方库文档查询。
> https://pkg.go.dev/

> 2: **Go 官方文档** 查语言特性、标准库和基础示例时很方便。
> https://go.dev/doc/

> 3: **Go by Example** Go 语言小例子非常全。
> https://gobyexample.com/

> 4: **Go Playground** 在线验证小段代码，分享 demo 很方便。
> https://go.dev/play/

> 5: **awesome-go** Go 生态工具与第三方库导航站。
> https://github.com/avelino/awesome-go

> 6: **StudyGolang / GolangBridge** 中文文章、经验分享和社区问答。
> https://studygolang.com/ > https://forum.golangbridge.org/

# 4：golang 常用库

> 1: **日志库**
> https://github.com/uber-go/zap > https://github.com/rs/zerolog > https://github.com/sirupsen/logrus

> 2: **配置库**
> https://github.com/spf13/viper > https://github.com/jinzhu/configor > https://github.com/knadh/koanf

> 3: **CLI 命令行**
> https://github.com/spf13/cobra > https://github.com/urfave/cli

> 4: **RPC 和微服务**
> https://github.com/grpc/grpc-go > https://github.com/asim/go-micro > https://go-kratos.dev/docs/getting-started/usage

> 5: **grpc 中间件**
> https://github.com/grpc-ecosystem/go-grpc-middleware

> 6: **数据库相关**
> mysql: https://github.com/go-xorm/xorm
> redis: https://github.com/gomodule/redigo
> mongo: https://github.com/qiniu/qmgo
> kafka: https://github.com/Shopify/sarama

> 7: **限流组件**
> https://github.com/uber-go/ratelimit > https://github.com/juju/ratelimit > https://github.com/RussellLuo/slidingwindow

> 8: **熔断组件**
> https://github.com/sony/gobreaker > https://github.com/afex/hystrix-go

> 9: **链路追踪**
> https://opentracing.io/ > https://opentelemetry.io/

> 10: **测试与压测**
> https://github.com/fortio/fortio > https://ghz.sh/ > https://github.com/fullstorydev/grpcui > https://github.com/uw-labs/bloomrpc

> 11: **性能可视化**
> https://github.com/arl/statsviz > https://github.com/go-echarts/statsview > https://github.com/parca-dev/parca

> 12: **其它好用库**
> https://github.com/go-playground/validator > https://github.com/samber/lo > https://github.com/shirou/gopsutil > https://github.com/go-echarts/go-echarts > https://github.com/golang-module/carbon