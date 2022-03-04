
- [1 c++ 配置 GRPC](#1-c-配置-grpc)
  - [1.1 setup dir](#11-setup-dir)
  - [1.2 install cmake](#12-install-cmake)
  - [1.3 Install other required tools](#13-install-other-required-tools)
  - [1.4 git clone grpc repo](#14-git-clone-grpc-repo)
  - [1.5 Build and install gRPC and Protocol Buffers](#15-build-and-install-grpc-and-protocol-buffers)
  - [1.6 编写 proto 文件](#16-编写-proto-文件)
  - [1.7 编写 server/client 文件](#17-编写-serverclient-文件)
  - [1.8 执行](#18-执行)
- [2 golang grpc 环境搭建](#2-golang-grpc-环境搭建)
  - [2.1 Prerequisites](#21-prerequisites)
    - [golang](#golang)
    - [protobuffer](#protobuffer)
  - [2.2 Get the example code](#22-get-the-example-code)

# 1 c++ 配置 GRPC

https://grpc.io/docs/languages/cpp/quickstart/

## 1.1 setup dir

```bash
export MY_INSTALL_DIR=$HOME/.local

mkdir -p $MY_INSTALL_DIR

export PATH="$MY_INSTALL_DIR/bin:$PATH"
```

## 1.2 install cmake

```bash
sudo apt install -y cmake
```

## 1.3 Install other required tools

```bash
sudo apt install -y build-essential autoconf libtool pkg-config

```

## 1.4 git clone grpc repo

```bash
git clone --recurse-submodules -b v1.41.0 https://github.com/grpc/grpc
```

## 1.5 Build and install gRPC and Protocol Buffers

```bash
cd grpc
mkdir -p cmake/build
pushd cmake/build
cmake -DgRPC_INSTALL=ON \
    -DgRPC_BUILD_TESTS=OFF \
    -DCMAKE_INSTALL_PREFIX=$MY_INSTALL_DIR \
    ../..
make -j
make install
popd
```

```bash
# cmake
mkdir -p cmake/build
cd cmake/build
cmake ../..
make
```

## 1.6 编写 proto 文件

## 1.7 编写 server/client 文件

## 1.8 执行

# 2 golang grpc 环境搭建

https://grpc.io/docs/languages/go/quickstart/

## 2.1 Prerequisites

### golang

- golang 开发环境

### protobuffer

- protoc (protocol buffer 编译器，v3)
- Go plugins for the protocol compiler (go 插件...)
  ```go
  go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.26
  go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.1
  ```

## 2.2 Get the example code

```go
 git clone -b v1.41.0 https://github.com/grpc/grpc-go
```
