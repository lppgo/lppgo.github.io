---
title: "goplugin功能"
author: "lucas(lpp)"
date: 2022-09-20
lastmod: 2022-09-20

categories: ["Go"]
tags: ["Go", "so", "plugin", "共享库"]
keywords: ["go", "共享库"]
---

<div align="center"><font size="35">Go Plugin插件(so动态库)</font></div>

# 1: 官方实现

- golang 1.8 及以上版本提供了一个创建共享库（shared object）的新工具，称为 Plugins。
- 目前 Plugins 仅在 Linux、FreeBSD 和 macOS 上受支持，且只支持 golang 调用。

# 2: 使用示例，定义一个 plugin.go

```go
package main

import (
	"log"
)

func init() {
	log.Println("plugin init")
}

type SayHello struct {
}

func (s *SayHello) CallMe(name string) string {
	log.Println("hello ", name)
	return "I am plugin"
}

// SayHelloPlugin 导出变量
var SayHelloPlugin SayHello

/*
使用 -buildmode=plugin 模式编译出 plugin.so 共享库
go build -o plugin.so -buildmode=plugin plugin.go

*/

```

- 使用 -buildmode=plugin 模式编译出 plugin.so 共享库;
- `go build -o plugin.so -buildmode=plugin plugin.go`

# 3: main.go 中调用插件(共享库)

```go
package main

import (
	"log"
	"plugin"
)

type CustomPlugin interface {
	CallMe(name string) string
}

func main() {
	// 打开插件（并发安全）
	p, err := plugin.Open("plugin.so")
	if err != nil {
		panic(err)
	}
	// 在插件中搜索可导出的变量或函数
	sayHelloPlugin, err := p.Lookup("SayHelloPlugin")
	if err != nil {
		panic(err)
	}
	// 断言插件类型
	if sayHello, ok := sayHelloPlugin.(CustomPlugin); ok {
		log.Println(sayHello.CallMe("togettoyou"))
	}
}

// go run main.go
// # 输出
// 2021/07/28 17:07:21 plugin init
// 2021/07/28 17:07:21 hello  togettoyou
// 2021/07/28 17:07:21 I am plugin

```

# 4:定义一个插件共享库总结：

```go
package 包名需要定义为 main

必须有可导出的变量或函数

不需要 main 函数

插件加载时会先执行 init 函数
```

# 5:Traefik Yaegi 实现

- yaegi 是一个 go 解释器;
- https://github.com/traefik/yaegi
- Yaegi 运行在 Go 运行时之上，可以直接作为嵌入式解释器，或使用交互式 shell ，解释运行 Go 代码

## 5.1 代码结构

- 这里有个注意点，Yaegi 的插件需要放在 src 目录下;

```go
│  go.mod
│  go.sum
│  main.go
│
└─plugin
    └─src
        └─hello
                go.mod
                hello.go
```

## 5.2 hello.go

```go
package hello

import (
 "fmt"
)

func init() {
 fmt.Println("hello plugin init")
}

func CallMe(msg string) string {
 fmt.Println(msg)
 return "I am plugin"
}
```

## 5.3 main.go

```go
package main

import (
 "fmt"
 "github.com/traefik/yaegi/interp"
 "github.com/traefik/yaegi/stdlib"
)

func main() {
 // 初始化解释器
 i := interp.New(interp.Options{GoPath: "./plugin/"})

 // 插件需要使用标准库
 if err := i.Use(stdlib.Symbols); err != nil {
  panic(err)
 }

 // 导入 hello 包
 if _, err := i.Eval(`import "hello"`); err != nil {
  panic(err)
 }

 // 调用 hello.CallMe
 v, err := i.Eval("hello.CallMe")
 if err != nil {
  panic(err)
 }
 callMe := v.Interface().(func(string) string)
 fmt.Println(callMe("togettoyou"))
}
go run main.go

# 输出
hello plugin init
togettoyou
I am plugin
```
