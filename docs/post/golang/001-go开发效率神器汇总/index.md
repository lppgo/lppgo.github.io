
# Table of Contents

- [Table of Contents](#table-of-contents)
- [1：开发工具](#1开发工具)
- [2：调试工具](#2调试工具)
- [3：网络工具](#3网络工具)

# 1：开发工具

> 1: **sql2go** sql 语句转换为 Go 结构体，使用 ddl。
> http://stming.cn/tool/sql2go.html

> 2: **json2go** 将 json 格式转为 Go struct
> https://mholt.github.io/json-to-go/

> 3: **toml2go** 将编码后的 toml 文本转为 Go struct
> https://xuri.me/toml-to-go/

> 4: **curl2go** 将 curl 命令转为 go 代码
> https://mholt.github.io/curl-to-go/

> 5: **msql 转 ES** sql 语句转换为 ES 语句.
> http://www.ischoolbar.com/EsParser/

> 6: **go 压缩解压库** 一个好用的文件压缩和解压工具，集成了 zip，tar 等多种功能，主要还有跨平台。
> https://github.com/mholt/archiver

> 7: **热编译工具** sql 语句转换为 Go 结构体，使用 ddl。
> https://github.com/silenceper/gowatch

> 7: **revive** golang 代码质量检测工具
> https://github.com/mgechev/revive

> 8: **Go Callvis** golang 的代码调用链图工具
> https://github.com/TrueFurby/go-callvis

> 9: **gotests** 自动生成测试用例工具
> https://github.com/cweill/gotests

> 10: **gomodifytags** Go tool to modify struct field tags
> https://github.com/fatih/gomodifytags

# 2：调试工具

> 1: **perf**
> 代理工具，支持内存，cpu，堆栈查看，并支持火焰图.
> perf 工具和 go-torch 工具，快捷定位程序问题.
> https://github.com/uber-archive/go-torch > https://github.com/google/gops

> 2: **dlv 远程调试**
> 基于 goland+dlv 可以实现远程调式的能力.
> https://github.com/go-delve/delve
> 提供了对 golang 原生的支持，相比 gdb 调试，简单太多。

> 3: **网络代理工具**
> goproxy 代理，支持多种协议，支持 ssh 穿透和 kcp 协议.
> https://github.com/snail007/goproxy

> 4: **抓包工具**
> go-sniffer 工具，可扩展的抓包工具，可以开发自定义协议的工具包. 现在只支持了 http，mysql，redis，mongodb.
> 基于这个工具，我们开发了 qapp 协议的抓包。
> https://github.com/40t/go-sniffer

> 6: **反向代理工具 ngrok**，快捷开放内网端口供外部使用。
> ngrok 可以让内网服务外部调用
> https://ngrok.com/ > https://github.com/inconshreveable/ngrok

> 7: **配置化生成证书**
> 从根证书，到业务侧证书一键生成.
> https://github.com/cloudflare/cfssl

> 8: **免费的证书获取工具**
> 基于 acme 协议，从 letsencrypt 生成免费的证书，有效期 1 年，可自动续期。
> https://github.com/Neilpang/acme.sh

> 8: **开发环境管理工具 vagrant**，单机搭建可移植工具的利器。支持多种虚拟机后端。
> vagrant 常被拿来同 docker 相比，值得拥有。
> https://github.com/hashicorp/vagrant

> 9: **轻量级容器调度工具 nomad**
> nomad 可以非常方便的管理容器和传统应用，相比 k8s 来说，简单不要太多.
> https://github.com/hashicorp/nomad

> 10: **高度可配置化的 http 转发工具**，基于 etcd 配置。
> https://github.com/gojek/weaver

> 11: **进程监控工具 supervisor** > https://www.jianshu.com/p/39b476e808d8

> 12: **基于 procFile 进程管理工具**. 相比 supervisor 更加简单。
> https://github.com/ddollar/foreman

> 13: **基于 http，https，websocket 的调试代理工具**，配置功能丰富。在线教育的 nohost web 调试工具，基于此开发.
> https://github.com/avwo/whistle

> 14: **分布式调度工具** > https://github.com/shunfei/cronsun/blob/master/README_ZH.md > https://github.com/ouqiang/gocron

> 15: **自动化运维平台 Gaia** > https://github.com/gaia-pipeline/gaia

> 16: **heimdall** 一个增强型 http 库，具有(断路器，retry mechanism)
> https://github.com/gojek/heimdall

# 3：网络工具

![](https://i0.hdslb.com/bfs/album/012a0b147350aeafa4f92fe5f197d71641018b2e.jpg)
