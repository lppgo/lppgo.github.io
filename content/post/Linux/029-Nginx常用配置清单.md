---
title: "01-Nginx 常用配置清单.md"
author: "lucas"
date: 2021-06-06
lastmod: 2021-09-01

tags: ["Linux", "Nginx"]
categories: ["Linux"]
keywords: ["Nginx"]
---

Table of Contents

- [1: Nginx 配置](#1-nginx-配置)
- [2: Listen Port](#2-listen-port)
- [3: Access Log](#3-access-log)
- [4: Domain Name](#4-domain-name)
- [5: Static Asset](#5-static-asset)
- [6: Redirect](#6-redirect)
- [7: Reverse Proxy](#7-reverse-proxy)
- [8: Load Balance](#8-load-balance)
  - [8.1 RoundRobin 轮询(default)](#81-roundrobin-轮询default)
  - [8.2 weight (权重)](#82-weight-权重)
  - [8.3 ip_hash（IP 绑定 ip_hash ）](#83-ip_haship-绑定-ip_hash-)
  - [8.4 url_hash](#84-url_hash)
  - [8.5 fair（第三方）](#85-fair第三方)
- [9: SSL 协议](#9-ssl-协议)
- [10: Nginx 加速](#10-nginx-加速)
  - [10.1 启用 Gzip 压缩](#101-启用-gzip-压缩)
  - [10.2 设置缓存头](#102-设置缓存头)
  - [10.3 启用 HTTP2 协议](#103-启用-http2-协议)
  - [10.4 优化日志 Optimizing Logging](#104-优化日志-optimizing-logging)
    - [10.4.1 禁用页面资源请求的日志记录](#1041-禁用页面资源请求的日志记录)
    - [10.4.2 禁用成功请求的日志记录](#1042-禁用成功请求的日志记录)
    - [10.4.3 最小化 I/O 操作](#1043-最小化-io-操作)
  - [10.5 限制带宽](#105-限制带宽)
- [11: location 语法](#11-location-语法)
- [12: nginx 高可用 keepalived](#12-nginx-高可用-keepalived)

# 1: Nginx 配置

- 1: `/etc/nginx/conf.d/xxx.conf`
- 2: 在`/etc/nginx/nginx.conf`文件中有一行就是把刚刚配置的引进总的 nginx 配置中
  ` include /etc/nginx/conf.d/*.conf;`
- 3: 配置完成后重新启动 nginx

```bash
nginx -s reopen #重启Nginx

nginx -s reload #重新加载Nginx配置文件，然后以优雅的方式重启Nginx

nginx -s stop #强制停止Nginx服务

nginx -s quit #优雅地停止Nginx服务（即处理完所有请求后再停止服务）

nginx -?,-h #打开帮助信息

nginx -v #显示版本信息并退出

nginx -V #显示版本和配置选项信息，然后退出

nginx -t #检测配置文件是否有语法错误，然后退出

nginx -T #检测配置文件是否有语法错误，转储并退出

nginx -q #在检测配置文件期间屏蔽非错误信息

nginx -p prefix #设置前缀路径(默认是:/usr/share/nginx/)

nginx -c filename #设置配置文件(默认是:/etc/nginx/nginx.conf)

nginx -g directives #设置配置文件外的全局指令

killall nginx #杀死所有nginx进程
```

# 2: Listen Port

监听端口

```bash
server {
    # Standard HTTP Protocol
    listen 80;
    # Standard HTTPS Protocol
    listen 443 ssl;
    # For http2
    listen 443 ssl http2;
    # Listen on 80 using IPv6
    listen [::]:80;
    # Listen only on using IPv6
    listen [::]:80 ipv6only=on;
}
```

# 3: Access Log

访问日志

```bash
server {
    # Relative or full path to log file
    access_log /path/to/file.log;
    # Turn 'on' or 'off'
    access_log on;
}
```

# 4: Domain Name

域名

```bash
server {
    # Listen to yourdomain.com
    server_name yourdomain.com;
    # Listen to multiple domains  server_name yourdomain.com www.yourdomain.com;
    # Listen to all domains
    server_name *.yourdomain.com;
    # Listen to all top-level domains
    server_name yourdomain.*;
    # Listen to unspecified Hostnames (Listens to IP address itself)
    server_name "";
}
```

# 5: Static Asset

静态资源

```bash
server {
    listen 80;
    server_name yourdomain.com;
    location / {
    root /path/to/website;
    }
}
```

# 6: Redirect

重定向

```bash
server {
    listen 80;
    server_name www.yourdomain.com;
    return 301 http://yourdomain.com$request_uri;
}
server {
    listen 80;
    server_name www.yourdomain.com;
    location /redirect-url {
        return 301 http://otherdomain.com;
    }
}
```

# 7: Reverse Proxy

反向代理

```bash
server {
    listen 80;
    server_name yourdomain.com;
    location / {
        proxy_pass http://0.0.0.0:3000;
        # where 0.0.0.0:3000 is your application server (Ex: node.js) bound on 0.0.0.0 listening on port 3000
    }
}
```

# 8: Load Balance

- 1. 在 http 节点下，加入 upstream 节点
- 2. 将 server 节点下的 location 节点中的 proxy_pass 配置为：http:// + upstream 名称，即"http://backserver"

## 8.1 RoundRobin 轮询(default)

```bash
upstream backserver {
    server 10.0.6.108:7080;
    server 10.0.0.85:8980;
}
server {
    listen 80;
    server_name yourdomain.com;
    location / {
        proxy_pass http://backserver;
    }
}
```

## 8.2 weight (权重)

```bash
# 指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况
upstream backserver{
      server 10.0.0.77 weight=5;
      server 10.0.0.88 weight=10;
}
```

## 8.3 ip_hash（IP 绑定 ip_hash ）

```bash
# 每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。
upstream backserver {
ip_hash;
server 192.168.0.14:88;
server 192.168.0.15:80;
}
```

## 8.4 url_hash

```bash
# 按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。
```

## 8.5 fair（第三方）

```bash
# 按后端服务器的响应时间来分配请求，响应时间短的优先分配。
upstream backserver {
fair;
server server1;
server server2;
}
```

# 9: SSL 协议

```bash
server {
    listen 443 ssl;
    server_name yourdomain.com;
    ssl on;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/privatekey.pem;
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /path/to/fullchain.pem;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_session_timeout 1h;
    ssl_session_cache shared:SSL:50m;
    add_header Strict-Transport-Security max-age=15768000;
}
# Permanent Redirect for HTTP to HTTPS
server
{
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}
```

# 10: Nginx 加速

## 10.1 启用 Gzip 压缩

```bash
gzip on;
gzip_types application/xml
    application/json
    text/css
    text/javascript
    application/javascript;
gzip_vary on;
gzip_comp_level 6; //压缩比
gzip_min_length 500; //设置压缩最小单位，小于不压缩
```

## 10.2 设置缓存头

`Setting Cache Headers`
浏览器检索网页文件时，会将副本保留在本地磁盘缓存中。这样，当你再次访问该页面时，浏览器就不必从服务器重新获取文件。每个浏览器都有自己的使用逻辑，来决定何时使用该文件对应的本地副本，以及何时在服务器更改了该文件时再次获取它。但是，作为网站所有者，你可以在发送的 HTTP 响应中设置缓存控制和过期标头，以提高浏览器的缓存行为的效率，从而减少很多不必要的 HTTP 请求。

首先，可以为字体和图像设置较长的缓存过期时间，这些字体和图像可能不会经常更改。在下面的示例中，设置客户端浏览器将字体和图像在本地缓存中保留一个月。

```bash
location ~* \.(?:jpg|jpeg|gif|png|ico|woff2)$ {
    expires 1M;
    add_header Cache-Control "public";
}
```

## 10.3 启用 HTTP2 协议

```bash
listen 443 ssl http2;
```

## 10.4 优化日志 Optimizing Logging

我们在管理网站的时候，即使是有对应的监控服务，但是对应日志分析还是不够到位。你也可能只关注错误(400 和 500 个状态码等等)，而不是成功的请求。通过减少不必要的日志记录，可以节省服务器上的磁盘存储、CPU 和 I/O 操作。这不仅可以让我们服务器更快一些，而且释放的资源可以用来运行其他服务。

有几种不同的方法可以减少和优化日志记录，但是在这里，我们重点介绍三个。

### 10.4.1 禁用页面资源请求的日志记录

```bash
# 如果我们不需要记录检索普通页面资源的请求，比如图像文件、JavaScript 文件和 CSS 文件等等，
# 那么这是一个快速而简单的解决方案。你所需要做的就是创建一个与这些文件类型匹配的 location 块，并配置禁用其中的日志记录。
location ~* \.(?:jpg|jpeg|gif|png|ico|woff2|js|css)$ {
    access_log off;
}
```

### 10.4.2 禁用成功请求的日志记录

这是一种更好的方法，因为它会丢弃带有 2xx 或 3xx 的响应查询，仅记录错误请求。它比方法 1 稍微复杂一点，因为它取决于您的 Nginx 日志记录的配置方式。

使用 Nginx 官方文档中的示例，让我们打开条件日志记录。创建一个 $loggable 的变量并将其设置为 0，用于带有 2xx 和 3xx 响应代码的日志请求，否则设置为 1，即可。然后在 access_log 指令中，将该变量作为条件引用。

```bash
# /etc/nginx/nginx.conf
access_log /var/log/nginx/access.log;

# access_log directive
map $status $loggable {
    ~^[23] 0;
    default 1;
}

access_log /var/log/nginx/access.log combined if=$loggable;
```

### 10.4.3 最小化 I/O 操作

即使你要记录所有请求，也可以通过打开访问日志缓冲来最大程度地减少 I/O 操作。使用此指令，Nginx 将等待将日志数据写入磁盘，直到填满 512KB 缓冲区或自上次刷新以来已过了 1 分钟（以先发生者为准）

```bash
access_log /var/log/nginx/access.log combined buffer=512k flush=1m;
```

## 10.5 限制带宽

> Limiting Bandwidth for Particular URLs

使用 limit_rate 指令来限制特定 URL 的带宽。在这里，我们将 /download 下每个文件的传输速率限制为每秒 50KB 的速度。

```bash
location /download/ {
    limit_rate 50k;
}
```

你可能还希望仅对较大的文件进行速率限制，这可以通过 limit_rate_after 指令进行。在此示例中，每个文件(来自任何目录)的前 500KB 都不受速度限制地进行传输，之后的所有内容均以 50KB/s 的速度为上限。这样可以加快网站关键部分的交付速度，同时降低其他部分的速度。

```bash
location / {
    limit_rate_after 500k;
    limit_rate 50k;
}
```

> 请注意，速率限制仅适用于浏览器和 Nginx 之间的单个 HTTP 连接

# 11: location 语法

- location 指令用来 match url
- 语法如下:

```bash
location[ = | ~ | ~* | ^~] url{

}

=:用于不含正则表达式的url前，要求字符串与url严格匹配，匹配成功就停止向下搜索并处理请求
~：用于表示url包含正则表达式，并且区分大小写。
~*：用于表示url包含正则表达式，并且不区分大瞎写
^~：用于不含正则表达式的url前，要求ngin服务器找到表示url和字符串匹配度最高的location后，立即使用此location处理请求，而不再匹配
如果有url包含正则表达式，不需要有~开头标识
```

# 12: nginx 高可用 keepalived

- 准备 2 台 Nginx 服务器
- 安装 keepalived
- 虚拟 IP
