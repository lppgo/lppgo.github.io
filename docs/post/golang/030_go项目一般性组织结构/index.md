
<div align="center"><font size="35">Go项目一般性组织结构</font></div>

# 1: summary

# 2: 其他一些规划方案

# 3：自己的规划组织方式

```go
├── cmd/
│   └── main.go //启动函数
├── server                 // 对外的服务，比如微服务，rpc
│   └── rpc
│   └── micro
├── pkg
    ├── common  // 全局
    │   └── conf
    │   └── log
    │   └── db
    │   └── redis
    │   └── globalvaribal
    │   └── const
    ├── internal/
    │       └── service/
    │           └── xxx_service.go //业务逻辑处理类
    │           └── xxx_service_test.go
    │       └── model/
    │           └── xxx_info.go//结构体
    │       └── api/
    │           └── xxx_api.go//路由对应的接口实现
    │       └── router/
    │           └── router.go//路由
    │       └── tools/   // 服务内部的一些公共工具,方法和函数
    │           └── datetool//时间工具类
    │           └── jsontool//json 工具类
```
