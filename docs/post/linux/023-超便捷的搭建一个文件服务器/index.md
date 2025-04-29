
- [1: 使用python快速搭建](#1-使用python快速搭建)
- [2: 使用darkhttpd](#2-使用darkhttpd)
  - [2.1 安装darkhttpd](#21-安装darkhttpd)

# 1: 使用python快速搭建
> 1: 进入目录
> 2: python启动httpp 文件服务器

```bash
# python2
 python -m SimpleHTTPServer
# python3
 python3 -m http.server

```
> 3: 通过 curl 或者浏览器访问命令执行文件夹下面的文件

# 2: 使用darkhttpd 
- 给大家一个类似的工具 darkhttpd，使用 C 编写的文件服务器，编译后为一个二进制文件无任何依赖，同时性能高和资源占用极低，非常适合在各种嵌入式设备上使用

## 2.1 安装darkhttpd

[darkhttpd](https://github.com/4kercc/darkhttpd)


[docker aria2 and darkhttpd](https://github.com/test482/docker-aria2-and-darkhttpd)




