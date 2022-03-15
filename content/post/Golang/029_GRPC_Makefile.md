---
title: "02-GRPC_Makefile"
author: "lucas(lpp)"
date: 2022-03-15
lastmod: 2022-03-15

categories: ["Go"]
tags: ["grpc", "make"]
keywords: ["grpc", "makefile"]
---

<div align="center"><font size="35">GRPC Makefile脚本</font></div>

- `Makefile`文件内容如下：

```makefile

GOPATH:=$(shell go env GOPATH)
VERSION=$(shell git describe --tags --always)
INTERNAL_PROTO_FILES=$(shell find internal -name *.proto)
API_PROTO_FILES=$(shell find proto -name *.proto)



.PHONY: init
# init env
init:
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
	go install go.unistack.org/protoc-gen-go-micro/v3@latest
	go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@latest
	go install github.com/google/gnostic/cmd/protoc-gen-openapi@latest


.PHONY: config
# generate internal proto

.PHONY: api
# generate api proto
api:
	protoc --proto_path=. \
	       --proto_path=./third_party \
 	       --go_out=paths=import:. \
 	       --go-http_out=paths=import:. \
 	       --go-grpc_out=paths=import:. \
 	       --go-micro_out=debug=true,,components="micro",paths=import:. \
	       $(API_PROTO_FILES)

 	    #    --go-micro_out=debug=true,,components="micro|http",paths=source_relative:./go_proto
		#    --openapi_out==paths=source_relative:./go_proto
		#    --swagger_out=logtostderr=true:./go_proto

.PHONY: clean
# rm -rf "./go_proto/pb"
clean:
	find ./go_proto -name "*.pb.go" | xargs rm -f

.PHONY: build
# build
build:
	mkdir -p bin/ && go build -ldflags "-X main.Version=$(VERSION)" -o ./bin/ ./...

.PHONY: generate
# generate
generate:
	go generate ./...

.PHONY: all
# generate all
all:
	make api;
	# make generate;

.PHONY: help
# show help
help:
	@echo ''
	@echo 'Usage:'
	@echo ' make [target]'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
	helpMessage = match(lastLine, /^# (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 2, RLENGTH); \
			printf "\033[36m%-22s\033[0m %s\n", helpCommand,helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help



```
