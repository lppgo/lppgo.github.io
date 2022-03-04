---
title: "01-go使用Linux内核端口复用进行LoadBalance"
author: "lucas"
date: 2021-10-12
lastmod: 2021-10-12

tags: ["Go"]
categories: ["Go"]
keywords: ["负载均衡", "端口复用"]
---

- [1 查看 Linux Kernal](#1-查看-linux-kernal)
- [2 Golang 如何使用端口复用](#2-golang-如何使用端口复用)
  - [2.1 说明](#21-说明)
  - [2.2 Go ReusePort](#22-go-reuseport)
    - [2.2.1 go server](#221-go-server)
    - [2.2.2 调用测试](#222-调用测试)
    - [2.2.3 端口复用 REUSEPORT 好处](#223-端口复用-reuseport-好处)

# 1 查看 Linux Kernal

- socket 五元组 `{<protocol>, <src addr>, <src port>, <dest addr>, <dest port>}`
- `uname -a`
- Linux 3.9 内核引入了 `SO_REUSEPORT`选项，可支持多个进程或者线程绑定到同一个端口，用于提高服务器的性能。他的特性包含一下几点:
  - 允许多个 socket 套接字 bind 同一个 TCP/UDP 端口；
    - 每一个线程拥有自己的服务器套接字;
    - 在服务器套接字上没有了锁的竞争；
  - 内核层面实现负载均衡；
  - 安全层面，listen 同一个端口的 socket 套接字只能位于同一个 user 下。
- 有了`SO_RESUEPORT`后，每个进程可以 bind 相同的地址和端口，各自是独立平等的；
- 让多进程监听同一个端口，各个进程中 accept socket fd 不一样，有新连接建立时，内核只会调度一个进程来 accept，并且保证调度的均衡性。

![端口复用图示](/images/端口复用20211012.webp)

# 2 Golang 如何使用端口复用

## 2.1 说明

- Linux 经典的设计哲学：一切皆文件。当然，socket 也不例外，它也是一种文件。
- 如果我们想在 Go 程序中，利用上 linux 的 SO_REUSEPORT 选项，那就需要有修改内核 socket 连接选项的接口，而这可以依赖于 golang.org/x/sys/unix 库来实现，具体就在以下这个方法。

```go
import “"golang.org/x/sys/unix"”
...
unix.SetsockoptInt(int(fd), unix.SOL_SOCKET, unix.SO_REUSEPORT, 1)
```

## 2.2 Go ReusePort

### 2.2.1 go server

```go
package main

import (
	"context"
	"fmt"
	"net"
	"net/http"
	"os"
	"syscall"

	"golang.org/x/sys/unix"
)

var lc = net.ListenConfig{
	Control: func(network, address string, c syscall.RawConn) error {
		var opErr error
		if err := c.Control(func(fd uintptr) {
			opErr = unix.SetsockoptInt(int(fd), unix.SOL_SOCKET, unix.SO_REUSEPORT, 1)
		}); err != nil {
			return err
		}
		return opErr
	},
}

func main() {
	pid := os.Getpid()
	l, err := lc.Listen(context.Background(), "tcp", "127.0.0.1:8000")
	if err != nil {
		panic(err)
	}
	server := &http.Server{}
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintf(w, "Client [%s] Received msg from Server PID: [%d] \n", r.RemoteAddr, pid)
	})
	fmt.Printf("Server with PID: [%d] is running \n", pid)
	_ = server.Serve(l)
}
```

### 2.2.2 调用测试

- 编译 `CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go`
- 启动服务

```go
~ $ ./main
Server with PID: [32687] is running
~ $ ./main
Server with PID: [32691] is running
~ $ ./main
Server with PID: [32697] is running
```

- 使用 curl 命令，模拟多次请求

```go
 for i in {1..20}; do curl localhost:8000; done
Client [127.0.0.1:56876] Received msg from Server PID: [32697]
Client [127.0.0.1:56880] Received msg from Server PID: [32687]
Client [127.0.0.1:56884] Received msg from Server PID: [32687]
Client [127.0.0.1:56888] Received msg from Server PID: [32687]
Client [127.0.0.1:56892] Received msg from Server PID: [32691]
Client [127.0.0.1:56896] Received msg from Server PID: [32697]
Client [127.0.0.1:56900] Received msg from Server PID: [32691]
Client [127.0.0.1:56904] Received msg from Server PID: [32691]
Client [127.0.0.1:56908] Received msg from Server PID: [32697]
Client [127.0.0.1:56912] Received msg from Server PID: [32697]
Client [127.0.0.1:56916] Received msg from Server PID: [32687]
Client [127.0.0.1:56920] Received msg from Server PID: [32691]
Client [127.0.0.1:56924] Received msg from Server PID: [32697]
Client [127.0.0.1:56928] Received msg from Server PID: [32697]
Client [127.0.0.1:56932] Received msg from Server PID: [32691]
Client [127.0.0.1:56936] Received msg from Server PID: [32697]
Client [127.0.0.1:56940] Received msg from Server PID: [32687]
Client [127.0.0.1:56944] Received msg from Server PID: [32691]
Client [127.0.0.1:56948] Received msg from Server PID: [32687]
Client [127.0.0.1:56952] Received msg from Server PID: [32697]
```

### 2.2.3 端口复用 REUSEPORT 好处

- 提高服务器程序的吞吐性能：我们可以运行多个应用程序实例，充分利用多核 CPU 资源，避免出现单核在处理数据包，其他核却闲着的问题；
- 内核级负载均衡：我们不需要在多个实例前面添加一层服务代理，因为内核已经提供了简单的负载均衡；
- 不停服更新：当我们需要更新服务时，可以启动新的服务实例来接受请求，再优雅地关闭掉旧服务实例
