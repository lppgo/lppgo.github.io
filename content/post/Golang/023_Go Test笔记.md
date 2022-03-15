---
title: "01-Go Test笔记"
author: "lucas"
date: 2021-12-21
lastmod: 2021-12-21

tags: ["test"]
categories: ["Go"]
keywords: ["test"]
---

<div align="center"><font size="35">Go Test笔记</font></div>

# Go Test

- 一个完整的单测指令可以是 `go test -v -cover -gcflags=all=-l -coverprofile=coverage.out`
- `-gcflags=all=-l` 防止编译器内联优化导致单测出现问题

## 1.1 go test

`go test -run=^TestDo -v ./`
这里介绍几个常用的参数：

- `-bench regexp` 执行相应的 benchmarks，例如 -bench=.；
- `-cover` 开启测试覆盖率；
- `-trace=copy_trace.out` 生成 trace.out 文件（go tool trace copy_trace.out）
- `-run regexp` 只运行 regexp 匹配的函数，例如 -run=Array 那么就执行包含有 Array 开头的函数；
- `-count` 执行次数。
- `-v` 显示测试的详细命令。

## 1.2 go test cover 生成测试覆盖度报告

`go tool cover -html=coverage.out`

```go
// 编写测试用例,(eg./microv3/service/api/auth/wrapper_test.go)

// 生成测试用例可执行文件xxx.test;生成覆盖率profile文件coverage.data
go test -c -covermode=count -coverpkg ./... -coverprofile=coverage.data ./

go test -covermode=count -coverprofile=cover.out ./...


// 执行测试可执行文件,执行单元测试，计算测试覆盖率
./xxx.test

// 将测试覆盖率profile文件输出为html文件，可在网页中直接查看各文件的测试覆盖情况
go tool cover -html=coverage.data -o coverage.html

go tool cover -html=cover.out -o coverage.html


go tool cover -html=api.test -o coverage2.html
```

## 1.3 go test 文件在项目中 layout
