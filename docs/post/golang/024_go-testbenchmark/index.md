
<div align="center"><font size="35">Go TestBenchmark笔记</font></div>
Table of Contents
=================

- [Table of Contents](#table-of-contents)
- [Go Test Benchmark](#go-test-benchmark)
  - [1.1 go test benchmark 示例](#11-go-test-benchmark-示例)
  - [1.2 go test benchmark benchstat 比较工具](#12-go-test-benchmark-benchstat-比较工具)

# Go Test Benchmark

- 在 Go 中，通过撰写 Benchmark 函数可以很方便地对某个功能点进行性能检测。对于重要的函数，我们可以在 CI/CD 中添加相应的测试流程，当函数性能发生变化时能够及时感知。那问题来了，如何检测函数的性能变化？
- 换个说法，你编写了某功能函数但发现它运行很慢，需要对该函数进行优化，当你在谷歌搜索找到更好的实现方式，通过 Benchmark 函数发现它的确变快了。但你说不清楚具体变快了多少，你想知道函数优化前后的性能对比，提高多少百分点，可信度高吗？
- 针对以上的需求场景，有一个工具可以帮助到你，它就是 **benchstat**

## 1.1 go test benchmark 示例

```go
// fib.go
func FibSolution(n int) int {
 if n < 2 {
  return n
 }

 return FibSolution(n-1) + FibSolution(n-2)
}

// fib_test.go
func BenchmarkFib20(b *testing.B) {
 for i := 0; i < b.N; i++ {
  FibSolution(20)
 }
}

// 命令行执行go test -bench=BenchmarkFib20得到性能结果
```

执行 `go test -bench=BenchmarkFib20` 得到性能结果：

```go
BenchmarkFib20-8           39452             30229 ns/op

// 其中，-8 代表的是 8 cpu，函数运行次数为 39452，每次函数的平均花费时间为 30229ns。
// 如果我们想得到多次样本数据，可以指定 go test 的 -count=N 参数。
// 例如想得到 5 次样本数据，则执行go test -bench=BenchmarkFib20 -count=5

BenchmarkFib20-8           39325             30297 ns/op
BenchmarkFib20-8           39216             30349 ns/op
BenchmarkFib20-8           39901             30251 ns/op
BenchmarkFib20-8           39336             30455 ns/op
BenchmarkFib20-8           39423             30894 ns/op
```

这里介绍几个常用的参数：

- `-bench regexp` 执行相应的 benchmarks，例如 -bench=.；
- `-cover` 开启测试覆盖率；
- `-trace=copy_trace.out` 生成 trace.out 文件（go tool trace copy_trace.out）
- `-run regexp` 只运行 regexp 匹配的函数，例如 -run=Array 那么就执行包含有 Array 开头的函数；
- `-count` 执行次数。
- `-v` 显示测试的详细命令。

## 1.2 go test benchmark benchstat 比较工具

**benchstat** 是 Go 官方推荐的一款命令行工具，它用于计算和比较基准测试的相关统计数据。

- 我们可以通过以下命令进行安装

```go
go install golang.org/x/perf/cmd/benchstat@latest
```

- 执行 -h 参数可以看到该工具的使用描述

```go
~ $ benchstat -h
usage: benchstat [options] old.txt [new.txt] [more.txt ...]
options:
  -alpha α
     consider change significant if p < α (default 0.05)
  -csv
     print results in CSV form
  -delta-test test
     significance test to apply to delta: utest, ttest, or none (default "utest")
  -geomean
     print the geometric mean of each file
  -html
     print results as an HTML table
  -norange
     suppress range columns (CSV only)
  -sort order
     sort by order: [-]delta, [-]name, none (default "none")
  -split labels
     split benchmarks by labels (default "pkg,goos,goarch")
```

- 我们想比较 FibSolution(n) 从 15 到 20，两种实现方式的性能基准测试。

```go
$ go test -bench=. -count=5 | tee old.txt
$ go test -bench=. -count=5 | tee new.txt

// 我们可以用benchstat对这两个函数实现逻辑进行性能对比
 $ benchstat old.txt new.txt
name     old time/op  new time/op  delta
Fib15-8  2.67µs ± 2%  0.01µs ± 5%  -99.81%  (p=0.008 n=5+5)
Fib16-8  4.20µs ± 1%  0.01µs ± 2%  -99.87%  (p=0.008 n=5+5)
Fib17-8  6.81µs ± 0%  0.01µs ± 2%  -99.92%  (p=0.008 n=5+5)
Fib18-8  11.1µs ± 1%   0.0µs ± 1%  -99.95%  (p=0.008 n=5+5)
Fib19-8  18.0µs ± 2%   0.0µs ± 4%  -99.97%  (p=0.008 n=5+5)
Fib20-8  29.2µs ± 1%   0.0µs ± 3%  -99.98%  (p=0.008 n=5+5)

// 可以看到，递归式实现的函数，他的执行时间随着 n 值变大增加非常明显。迭代式实现方式，相较于递归式，它的平均时间开销降低了 99 % 以上，优化效果非常明显。

// 另外，p=0.008 表示结果的可信程度，p 值越大表明可信度越低。一般以 0.05 作为临界值，超过该值，则结果不可信。n=5+5 表示分别使用的有效样本数量
```
