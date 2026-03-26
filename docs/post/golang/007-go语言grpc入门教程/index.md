
- [go 语言 grpc 入门教程](#go-语言-grpc-入门教程)
  - [1: 安装 go 语言 grpc 包](#1-安装-go-语言-grpc-包)
  - [2:安装 protobuf 编译器](#2安装-protobuf-编译器)
    - [2.1 安装 protoc 编译器](#21-安装-protoc-编译器)
    - [2.2 安装编译器 go 语言插件](#22-安装编译器-go-语言插件)
  - [3: Example 目录结构](#3-example-目录结构)
  - [4: 定义服务](#4-定义服务)
  - [5: 编译 proto 协议文件](#5-编译-proto-协议文件)
  - [6: 实现服务端代码](#6-实现服务端代码)
  - [7:实现客户端代码](#7实现客户端代码)
  - [8: 使用 grpc-gateway](#8-使用-grpc-gateway)
    - [8.1 安装 grpc-hateway](#81-安装-grpc-hateway)
  - [8.2 修改 x.proto 文件](#82-修改-xproto-文件)
  - [8.3 生成 pb.go 代码](#83-生成-pbgo-代码)

# go 语言 grpc 入门教程

> 前置知识点
> 1: [protobuf 语法](https://www.tizi365.com/archives/367.html)
> 2: [grpc 核心概念](https://www.tizi365.com/archives/391.html)

## 1: 安装 go 语言 grpc 包

```go
go get -u -v google.golang.org/grpc
```

## 2:安装 protobuf 编译器

### 2.1 安装 protoc 编译器

protobuf 编译器就叫 protoc.

```go
到下面github地址，根据自己的系统版本选择下载，解压缩安装即可

https://github.com/protocolbuffers/protobuf/releases

解压缩安装包之后，将 [安装目录]/bin 目录，添加到PATH环境变量。

- `protoc` https://github.com/protocolbuffers/protobuf
  - (1) 编译安装
  - (2) 直接安装编译好的包
```

### 2.2 安装编译器 go 语言插件

因为目前的 protoc 编译器，默认没有包含 go 语言代码生成器，所以需要单独安装插件

- (1) protoc-gen-go
- (2) protoc-gen-go-grpc
- (3) protoc-gen-go-micro
- (4) protoc-gen-go-gateway
- (5) protoc-gen-grpc-swagger

```go
go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
go get -u github.com/golang/protobuf/protoc-gen-go
go install google.golang.org/protobuf/cmd/protoc-gen-go
go install go.unistack.org/protoc-gen-go-micro/v3
```

安装 go 语言插件后，需要将 $GOPATH/bin 路径加入到 PATH 环境变量中。

## 3: Example 目录结构

本教程例子的目录结构如下：

```go
helloworld/
├── client.go - 客户端代码
├── go.mod  - go模块配置文件
├── proto     - 协议目录
│   ├── helloworld.pb.go - rpc协议go版本代码
│   └── helloworld.proto - rpc协议文件
└── server.go  - rpc服务端代码
```

初始化命令如下：

```go
# 创建项目目录
mkdir helloworld
# 切换到项目目录
cd helloworld
# 创建RPC协议目录
mkdir proto
# 初始化go模块配置，用来管理第三方依赖, 本例子，项目模块名是：tizi365.com/helloworld
go mod init tizi365.com/helloworld
```

## 4: 定义服务

> 定义服务，其实就是通过 protobuf 语法定义语言平台无关的接口.

文件: helloworld/proto/helloworld.proto

```protobuf
syntax = "proto3";
// 定义包名
package proto;

// 定义Greeter服务
service Greeter {
  // 定义SayHello方法，接受HelloRequest消息， 并返回HelloReply消息
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// 定义HelloRequest消息
message HelloRequest {
  // name字段
  string name = 1;
}

// 定义HelloReply消息
message HelloReply {
  // message字段
  string message = 1;
}
```

Greeter 服务提供了一个 SayHello 接口，请求 SayHello 接口，需要传递一个包含 name 字段的 HelloRequest 消息，返回包含 message 字段的 HelloReply 消息。

## 5: 编译 proto 协议文件

> 上面通过 proto 定义的接口，没法直接在代码中使用，因此需要通过 protoc 编译器，将 proto 协议文件，编译成 go 语言代码。

```go
# 切换到helloworld项目根目录，执行命令
protoc -I proto/ --go_out=plugins=grpc:proto proto/helloworld.proto

// protoc命令参数说明:

// -I 指定代码输出目录，忽略服务定义的包名，否则会根据包名创建目录
// --go_out 指定代码输出目录，格式：--go_out=plugins=grpc:目录名
// 命令最后面的参数是proto协议文件

```

编译成功后在 proto 目录生成了 helloworld.pb.go 文件，里面包含了，我们的服务和接口定义。

## 6: 实现服务端代码

文件:helloworld/server.go

```go
package main

import (
	"log"
	"net"

	"golang.org/x/net/context"
	// 导入grpc包
	"google.golang.org/grpc"
	// 导入刚才我们生成的代码所在的proto包。
        pb "tizi365.com/helloworld/proto"
	"google.golang.org/grpc/reflection"
)


// 定义server，用来实现proto文件，里面实现的Greeter服务里面的接口
type server struct{}

// 实现SayHello接口
// 第一个参数是上下文参数，所有接口默认都要必填
// 第二个参数是我们定义的HelloRequest消息
// 返回值是我们定义的HelloReply消息，error返回值也是必须的。
func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	// 创建一个HelloReply消息，设置Message字段，然后直接返回。
	return &pb.HelloReply{Message: "Hello " + in.Name}, nil
}

func main() {
	// 监听127.0.0.1:50051地址
	lis, err := net.Listen("tcp", "127.0.0.1:50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	// 实例化grpc服务端
	s := grpc.NewServer()

        // 注册Greeter服务
	pb.RegisterGreeterServer(s, &server{})

	// 往grpc服务端注册反射服务
	reflection.Register(s)

        // 启动grpc服务
	if err := s.Serve(lis); err != nil {
	    log.Fatalf("failed to serve: %v", err)
	}
}
```

运行服务:

```go
# 切换到项目根目录，运行命令
go run server.go
```

## 7:实现客户端代码

文件：helloworld/client.go

```go
package main

import (
	"log"
	"os"
	"time"

	"golang.org/x/net/context"
	// 导入grpc包
	"google.golang.org/grpc"
	// 导入刚才我们生成的代码所在的proto包。
        pb "tizi365.com/helloworld/proto"
)

const (
	defaultName = "world"
)

func main() {
	// 连接grpc服务器
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	// 延迟关闭连接
	defer conn.Close()

	// 初始化Greeter服务客户端
	c := pb.NewGreeterClient(conn)

	// 初始化上下文，设置请求超时时间为1秒
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	// 延迟关闭请求会话
	defer cancel()

	// 调用SayHello接口，发送一条消息
	r, err := c.SayHello(ctx, &pb.HelloRequest{Name: "world"})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}

	// 打印服务的返回的消息
	log.Printf("Greeting: %s", r.Message)
}
```

```go
# 切换到项目根目录，运行命令
go run client.go
```

## 8: 使用 grpc-gateway

### 8.1 安装 grpc-hateway

- https://github.com/grpc-ecosystem/grpc-gateway

```go
go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
go install github.com/golang/protobuf/protoc-gen-go
go install github.com/google/gnostic/cmd/protoc-gen-openapi@latest
// go install github.com/go-kratos/kratos/cmd/protoc-gen-go-http/v2@latest
// go install github.com/go-kratos/kratos/cmd/protoc-gen-go-errors/v2@latest
// go install
// 上面执行成功后会在 $GOBIN (/usr/local/go/bin)目录下面 生成3个二进制文件
protoc-gen-grpc-gateway
protoc-gen-grpc-swagger
protoc-gen-go
```

## 8.2 修改 x.proto 文件

```go
syntax = "proto3";

package hello;

import "google/api/annotations.proto";

message HelloRequest {
    string name = 1;
    int32 age = 2;
}
message HelloReply {
    string message = 1;
}
service HelloService {
    rpc SayHello (HelloRequest) returns (HelloReply){
        option (google.api.http) = {
            post:"/v1/examples/sayhello"
            body:"*"
        };
    }
}

```

## 8.3 生成 pb.go 代码

- 生成`xxx.pb.go`

```go
protoc -I. \
-I/usr/local/include \
-I$GOPATH/src \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--go_out=paths=source_relative:.  *.proto

```

- 生成`gw.pb.go`

```go
protoc -I. \
-I/usr/local/include \
-I$GOPATH/src \
-I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
--grpc-gateway_out=logtostderr=true:. *.proto
```

- 生成`swagger`,hello.swagger.json

```go
protoc -I/usr/local/include -I. \
  -I$GOPATH/src \
  -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
  --swagger_out=logtostderr=true:. *.proto
```
