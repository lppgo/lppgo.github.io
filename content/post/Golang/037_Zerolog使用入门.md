---
title: "Zerolog使用入门"
author: "lucas(lpp)"
date: 2026-03-24
lastmod: 2026-03-24

categories: ["Go"]
tags: ["Go", "zerolog", "log"]
keywords: ["zerolog"]
---

<div align="center"><font size="35">Zerolog使用入门</font></div>

# 1: 概述

- `zerolog` 是一个面向 Go 的结构化日志库，默认输出 JSON 格式;
- 它的核心卖点是高性能和低开销，比较适合接口服务、后台任务、网关等对吞吐比较敏感的场景;
- `zero` 这个名字通常对应它强调的 zero-allocation 设计思路;
- 原文参考: `https://mp.weixin.qq.com/s/H1dxnjjigyhW1RoTxIBB7w`

- 一般来说，业务日志想要做到可检索、可聚合、可观测，最好不要只输出一段纯文本，而是带上 level、time、request_id、service、latency 这类结构化字段。`zerolog` 在这类场景下会比较顺手。

# 2: 核心特点

- 默认输出 JSON，天然适合接入 ELK、Loki、Datadog 这类日志系统;
- 链式 API 简洁，追加字段很方便;
- 支持 `context`，适合传递请求级别字段;
- 支持采样，可以避免高频日志把磁盘打满;
- 支持 Hook，方便统一补充字段、脱敏、上报异常;
- 既可以输出机器友好的 JSON，也可以在开发环境切换成更易读的 console 格式。

- 从使用体验上看，`zerolog` 的一个优点是 typed field 很多，例如 `Str()`、`Int()`、`Dur()`、`Bool()` 等，写起来不啰嗦，同时也能避免一部分额外开销。

# 3: 安装

```go
go get github.com/rs/zerolog/log
```

- 如果你需要更完整地使用 `zerolog` 包中的能力，也会直接引入 `github.com/rs/zerolog`。

```go
import (
    "github.com/rs/zerolog"
    "github.com/rs/zerolog/log"
)
```

# 4: 快速上手

- `log.Info()`、`log.Warn()`、`log.Error()` 用来创建日志事件;
- `Str()`、`Int()`、`Float64()`、`Bool()` 等用来追加字段;
- `Msg()` 或 `Msgf()` 负责真正输出日志。

```go
package main

import (
    "errors"

    "github.com/rs/zerolog/log"
)

func main() {
    log.Info().Msg("service started")

    log.Warn().
        Str("module", "user").
        Float64("ratio", 0.82).
        Msg("cache hit ratio is low")

    err := errors.New("connect db timeout")
    log.Error().
        Err(err).
        Str("dsn", "mysql-main").
        Msg("db connect failed")
}
```

- 默认情况下，`zerolog` 会输出到 `stderr`，并自动带上 `level`、`time`、`message` 等字段;
- 这种 JSON 输出比较适合生产环境做统一采集。

```go
{"level":"info","time":"2026-03-24T10:00:00Z","message":"service started"}
{"level":"warn","module":"user","ratio":0.82,"time":"2026-03-24T10:00:00Z","message":"cache hit ratio is low"}
{"level":"error","error":"connect db timeout","dsn":"mysql-main","time":"2026-03-24T10:00:00Z","message":"db connect failed"}
```

# 5: 常用配置

- 很多项目在开发环境更喜欢可读性高一点的日志格式，这时可以配合 `ConsoleWriter` 使用;
- 同时也可以设置全局日志级别和时间格式。

```go
package main

import (
    "os"
    "time"

    "github.com/rs/zerolog"
    "github.com/rs/zerolog/log"
)

func main() {
    zerolog.TimeFieldFormat = time.RFC3339
    zerolog.SetGlobalLevel(zerolog.InfoLevel)

    output := zerolog.ConsoleWriter{Out: os.Stdout, TimeFormat: time.RFC3339}
    log.Logger = log.Output(output)

    log.Info().Str("service", "demo-api").Msg("server started")
}
```

- 开发环境使用 console 格式更容易阅读;
- 生产环境通常仍然建议输出 JSON，方便日志平台解析。

# 6: 日志级别

- `zerolog` 常见级别从低到高可以理解为:
  - `trace`
  - `debug`
  - `info`
  - `warn`
  - `error`
  - `fatal`
  - `panic`

- 一般建议:
  - 本地开发用 `DebugLevel`;
  - 测试和生产通常使用 `InfoLevel` 或 `WarnLevel`;
  - `fatal` 和 `panic` 会中断程序，业务代码里要谨慎使用。

```go
zerolog.SetGlobalLevel(zerolog.DebugLevel)
```

# 7: 添加调用者与结构化字段

- 如果你想快速定位日志来自哪一行代码，可以打开 `Caller()`;
- 如果想让字段更贴合自己的日志规范，也可以修改字段名;
- `Dict()` 适合组织嵌套结构的数据。

```go
package main

import (
    "os"

    "github.com/rs/zerolog"
)

func main() {
    zerolog.TimestampFieldName = "ts"
    zerolog.MessageFieldName = "msg"

    logger := zerolog.New(os.Stdout).With().
        Str("service", "order-api").
        Timestamp().
        Caller().
        Logger()

    logger.Info().
        Str("order_id", "A1001").
        Dict("metrics", zerolog.Dict().
            Int("retry", 2).
            Float64("cost_ms", 23.7)).
        Msg("create order success")
}
```

- 这种方式比较适合给每条日志都补上统一字段，例如服务名、实例名、机房等。

# 8: 采样

- 在高并发服务里，某些日志可能会刷得特别快;
- 如果不做限制，日志文件、磁盘和日志平台都会有压力;
- `zerolog` 内置的采样能力可以控制日志量。

```go
package main

import (
    "os"
    "time"

    "github.com/rs/zerolog"
)

func main() {
    logger := zerolog.New(os.Stdout).Sample(&zerolog.BurstSampler{
        Burst:  100,
        Period: time.Second,
        NextSampler: &zerolog.BasicSampler{
            N: 10,
        },
    })

    for i := 0; i < 1000; i++ {
        logger.Info().Int("i", i).Msg("high frequency log")
    }
}
```

- `BasicSampler{N: 100}` 可以理解为每 100 条记录 1 条;
- `BurstSampler` 适合突发流量场景，先放行一部分，再按比例继续采样。

# 9: Context 传递请求字段

- 在 Web 服务里，我们经常希望跨函数携带 `request_id`、`trace_id`、`user_id` 这类字段;
- `zerolog` 对 `context` 支持比较自然。

```go
package main

import (
    "context"
    "os"

    "github.com/rs/zerolog"
)

func main() {
    logger := zerolog.New(os.Stdout).With().Str("request_id", "req-10001").Logger()
    ctx := logger.WithContext(context.Background())

    someFunc(ctx)
}

func someFunc(ctx context.Context) {
    zerolog.Ctx(ctx).Info().Msg("query user profile")
}
```

- 一旦 logger 被放进 context，后续函数就不需要再手工一层层传 logger 了;
- 这在 HTTP 中间件、RPC 调用链里都很常用。

# 10: Hook

- Hook 可以理解为日志输出前的拦截器;
- 比较常见的用途有:
  - 补统一字段;
  - 过滤敏感信息;
  - 根据级别做错误上报;
  - 把不同日志路由到不同目的地。

```go
package main

import (
    "fmt"
    "os"

    "github.com/rs/zerolog"
)

type SeverityHook struct{}

func (h SeverityHook) Run(e *zerolog.Event, level zerolog.Level, msg string) {
    e.Str("severity", level.String())
    if level >= zerolog.ErrorLevel {
        fmt.Println("send error to sentry")
    }
}

func main() {
    logger := zerolog.New(os.Stdout).Hook(SeverityHook{})
    logger.Error().Str("module", "payment").Msg("call upstream failed")
}
```

- 如果你的项目已经有告警平台或者审计平台，Hook 往往是一个很好接入的点。

# 11: 同时输出控制台和文件

- 有些项目希望开发环境看 console，线上环境再落文件;
- 也有些传统部署方式需要同时保留本地日志文件。

```go
package main

import (
    "os"
    "time"

    "github.com/natefinch/lumberjack"
    "github.com/rs/zerolog"
)

func main() {
    consoleWriter := zerolog.ConsoleWriter{
        Out:        os.Stdout,
        TimeFormat: time.RFC3339,
    }

    fileWriter := &lumberjack.Logger{
        Filename:   "./logs/app.log",
        MaxSize:    100,
        MaxBackups: 7,
        MaxAge:     30,
        Compress:   true,
        LocalTime:  true,
    }

    multi := zerolog.MultiLevelWriter(consoleWriter, fileWriter)
    logger := zerolog.New(multi).With().Timestamp().Logger()

    logger.Info().Str("service", "report-job").Msg("job started")
}
```

- 如果应用运行在 Kubernetes 或 Docker 体系里，很多时候直接写 stdout/stderr 就够了;
- 如果是传统虚机部署，文件轮转仍然很常见。

# 12: 在 Gin 中集成 zerolog

- 在 Gin 项目里，比较常见的做法是替换默认 logger 和 recovery;
- 再配合 `trace_id`，把请求日志和 panic 日志串起来。

```go
package main

import (
    "net/http"
    "time"

    "github.com/gin-gonic/gin"
    "github.com/google/uuid"
    "github.com/rs/zerolog/log"
)

func ZeroLogMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        traceID := c.GetHeader("X-Trace-ID")
        if traceID == "" {
            traceID = uuid.NewString()
        }

        start := time.Now()
        c.Writer.Header().Set("X-Trace-ID", traceID)
        c.Set("trace_id", traceID)

        c.Next()

        log.Info().
            Str("trace_id", traceID).
            Str("method", c.Request.Method).
            Str("path", c.Request.URL.Path).
            Int("status", c.Writer.Status()).
            Dur("latency", time.Since(start)).
            Msg("http access")
    }
}

func main() {
    r := gin.New()
    r.Use(ZeroLogMiddleware())

    r.GET("/ping", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"message": "pong"})
    })

    _ = r.Run(":8080")
}
```

- 如果再补一个自定义 Recovery，中间件里还可以把 panic 堆栈、请求头、请求路径、trace_id 一起记下来;
- 这样线上排查问题会方便很多。

# 13: 总结

- `zerolog` 比较适合追求性能、结构化和可观测性的 Go 服务;
- 开发环境可以优先用 `ConsoleWriter`，生产环境建议保留 JSON 输出;
- 请求链路里尽量统一补充 `request_id` 或 `trace_id`;
- 高频日志记得考虑 sampling;
- 需要统一增强日志行为时，可以优先考虑 Hook。

- 如果你的项目只是一个简单脚本，`zerolog` 未必是唯一选择;
- 但如果项目已经开始关注检索、链路、监控、性能和日志治理，那它会是一个很实用的基础组件。
