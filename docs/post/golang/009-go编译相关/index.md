
- [1: go 交叉编译](#1-go-交叉编译)
  - [1.1 查看可支 platform](#11-查看可支-platform)
  - [1.2 Go 交叉编译命令](#12-go-交叉编译命令)
  - [1.3 编译命令](#13-编译命令)
  - [1.4 编译时传入参数](#14-编译时传入参数)
- [2: shell 脚本](#2-shell-脚本)
- [3: Makefile](#3-makefile)

# 1: go 交叉编译

## 1.1 查看可支 platform

```go
go tool dist list

// 支持的OS跟ARCH
```

## 1.2 Go 交叉编译命令

```go
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -a -o vp-server_linux_amd64
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build
```

## 1.3 编译命令

## 1.4 编译时传入参数

```go
var (
	VERSION    string
	BUILD_TIME string
	GO_VERSION string
)

func main() {
	fmt.Printf("%s\n%s\n%s\n", VERSION, BUILD_TIME, GO_VERSION)
}

// go build -ldflags "-X main.VERSION=1.0.0 -X 'main.BUILD_TIME=`date +"%Y-%m-%d %H:%M:%S"`' -X 'main.GO_VERSION=`go version`'"

```

```bash
# go
var (
	VERSION     string
	BUILD_TIME  string
	GO_VERSION  string
	COMMIT_ID   string
	AUTHOR      string
	BRANCH_NAME string
)

func init() {
	log.Infof("\nVERSION:%s \nBUILD_TIME:%s \nGO_VERSION:%s \nCOMMIT_ID:%s \nAUTHOR:%s \nBRANCH_NAME:%s\n",
		VERSION, BUILD_TIME, GO_VERSION, COMMIT_ID, AUTHOR, BRANCH_NAME)
}
# go build shell

#!/bin/sh

VERSION="v1.0.0"
BUILD_TIME=`date +"%Y-%m-%d %H:%M:%S"`
GO_VERSION=`go version`
COMMIT_ID=`git log |head -n 1| awk '{print $2;}'`
AUTHOR=`git log |head -n 3| grep Author| awk '{print $2;}'`
BRANCH_NAME=`git branch | awk '/\*/ { print $2; }'`

go build -ldflags \
"-X 'main.VERSION=${VERSION}' \
-X 'main.BUILD_TIME=${BUILD_TIME}' \
-X 'main.GO_VERSION=${GO_VERSION}' \
-X 'main.COMMIT_ID=${COMMIT_ID}' \
-X 'main.AUTHOR=${AUTHOR}' \
-X 'main.BRANCH_NAME=${BRANCH_NAME}' "
```

# 2: shell 脚本

```shell
#!/bin/bash
export LANG="en_US.UTF-8"

echo "开始编译vp-server项目... "
echo "----> 1: linux (64) ; "
echo "----> 2: windows (64) ; "
echo "----> 3: darwin (64) ; "

if read -p "======>请选择您要编译的环境 :" args
then
    echo "------> 你输入的环境是 $args <------"
else
    echo "\n抱歉，你输入超时了。"
fi

echo
projectName="video_server"

if [ $args -eq 1 ]; then
  CGO_ENABLED=0 GOOS=linux GOARCH=amd64    go build -v -a -o ${projectName}_linux_amd64
elif [ $args -eq 2 ]; then
  CGO_ENABLED=0 GOOS=windows GOARCH=amd64    go build -v -a -o ${projectName}_windows_amd64.exe
elif [ $args -eq 3 ]; then
  CGO_ENABLED=0 GOOS=darwin GOARCH=amd64    go build -v -a -o ${projectName}_darwin_amd64
else
    echo "输入的参数$args不正确，执行退出..."
    exit 1
fi
echo
echo "...build success!!! 编译成功..."
```

# 3: Makefile

```makefile
.PHONY: all build clean run check cover lint docker help
BIN_FILE=hello
all: check build
build:
	@go build -o "${BIN_FILE}"
clean:
	go clean
	rm --force "xx.out"
test:
	go test
check:
	go fmt ./
	go vet ./
cover:
	go test -coverprofile xx.out
	go tool cover -html=xx.out
run:
	./"${BIN_FILE}"
lint:
	golangci-lint run --enable-all
docker:
	@docker build -t leo/hello:latest .
help:
	@echo "make 格式化go代码 并编译生成二进制文件"
	@echo "make build 编译go代码生成二进制文件"
	@echo "make clean 清理中间目标文件"
	@echo "make test 执行测试case"
	@echo "make check 格式化go代码"
	@echo "make cover 检查测试覆盖率"
	@echo "make run 直接运行程序"
	@echo "make lint 执行代码检查"
	@echo "make docker 构建docker镜像"

```
