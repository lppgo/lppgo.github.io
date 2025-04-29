
<div align="center"><font size="35">git仓库gomod私有化</font></div>

# 1: go module 私有仓库使用

```go
(1) 修改hosts
(2)
go env -w GOINSECURE="gitlab.yuliangtec.cn"
go env -w GONOSUMDB="gitlab.yuliangtec.cn"
go env -w GONOPROXY="gitlab.yuliangtec.cn"
go env -w GOPRIVATE="gitlab.yuliangtec.cn"

// (3) go get
go get com.yuliangtec.luna.proto


// (4) git tag --> go get
go get com.yuliangtec.luna.proto@v1.0.0
```

# 2: 补充

## 2.1 协议

## 2.2 设置环境变量(上 1)

https://blog.csdn.net/L_K1028/article/details/105313293

https://blog.csdn.net/qingchuwudi/article/details/107119273
