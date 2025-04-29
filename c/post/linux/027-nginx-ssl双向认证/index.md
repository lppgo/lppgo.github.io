
# Table of Contents

- [Table of Contents](#table-of-contents)
- [1: Nginx SSL Setting](#1-nginx-ssl-setting)
- [2: openssl 配置准备](#2-openssl-配置准备)
- [3: 创建 CA 根级证书](#3-创建-ca-根级证书)
- [4: 创建 server 证书](#4-创建-server-证书)
- [5: 创建 client 证书](#5-创建-client-证书)
- [6: 配置 Nginx ssl](#6-配置-nginx-ssl)

# 1: Nginx SSL Setting

> **Nginx 对 SSL 双向认证支持的比较好，配置很简单：**

```bash
listen      443;
server_name test.com;

ssl on;
ssl_certificate server.crt; //server端公钥
ssl_certificate_key server.key; //server端私钥
ssl_client_certificate client.crt; //client端公钥
ssl_session_timeout 5m;
ssl_verify_client on; //开启client验证
```

# 2: openssl 配置准备

```go
// 1 修改openssl配置

vi /etc/pki/tls/openssl.cnf

// 2 找到这句注释掉，替换为下面那句

#default_ca      = CA_default
default_ca      = CA_linvo

// 3 把[ CA_default ]整个部分拷贝一份，改成上面的名字[ CA_linvo ]

修改里面的如下参数：

dir = /etc/pki/ca_linvo
certificate = $dir/root/ca.crt
private_key = $dir/root/ca.key

//  4 保存退出
```

# 3: 创建 CA 根级证书

```go
// 生成key:(生成密钥xxx.key)
openssl genrsa -out /etc/pki/ca_linvo/root/ca.key

// 生成csr:(根据密钥生成证书请求文件xxx.csr)
openssl req -new -key /etc/pki/ca_linvo/root/ca.key -out /etc/pki/ca_linvo/root/ca.csr

// 生成crt:(根据密钥xxx.key和证书请求文件xxx.scr 生成crt证书)
openssl x509 -req -days 3650 -in /etc/pki/ca_linvo/root/ca.csr -signkey /etc/pki/ca_linvo/root/ca.key -out /etc/pki/ca_linvo/root/ca.crt

// 生成crl：
openssl ca -gencrl -out /etc/pki/ca_linvo/root/ca.crl -crldays 7

生成的根级证书文件都在/etc/pki/ca_linvo/root/目录下

注意：创建证书时，建议证书密码设置长度>=6位，因为java的keytool工具貌似对它有要求。
```

# 4: 创建 server 证书

> **Create a self-signed certificate for server:**

```go
// 1 生成key：
openssl genrsa -out /etc/pki/ca_linvo/server/server.key

// 2 生成csr：
openssl req -new -key /etc/pki/ca_linvo/server/server.key -out /etc/pki/ca_linvo/server/server.csr

// 3 生成crt：
openssl ca
-in /etc/pki/ca_linvo/server/server.csr
-cert /etc/pki/ca_linvo/root/ca.crt
-keyfile /etc/pki/ca_linvo/root/ca.key
-out /etc/pki/ca_linvo/server/server.crt
-days 3650


说明：

1、这里生成的crt是刚才ca根级证书下的级联证书，其实server证书主要用于配置正常单向的https，所以不使用级联模式也可以：

openssl rsa -in /etc/pki/ca_linvo/server/server.key -out /etc/pki/ca_linvo/server/server.key
openssl x509 -req -in /etc/pki/ca_linvo/server/server.csr -signkey /etc/pki/ca_linvo/server/server.key -out /etc/pki/ca_linvo/server/server.crt -days 3650
2、-days 参数可根据需要设置证书的有效期，例如默认365天
```

# 5: 创建 client 证书

```go
// 生成key：
openssl genrsa -des3 -out /etc/pki/ca_linvo/client/client.key 1024

// 生成csr：
openssl req -new -key /etc/pki/ca_linvo/client/client.key -out /etc/pki/ca_linvo/client/client.csr

// 生成crt：
openssl ca -in /etc/pki/ca_linvo/client/client.csr -cert /etc/pki/ca_linvo/root/ca.crt -keyfile /etc/pki/ca_linvo/root/ca.key -out /etc/pki/ca_linvo/client/client.crt -days 3650


说明：

1、这里就必须使用级联证书，并且可以重复该步骤，创建多套client证书

2、生成crt时可能会遇到如下报错：

openssl TXT_DB error number 2 failed to update database
可参照这里进行操作。

我使用的是方法一，即将index.txt.attr中unique_subject = no
```

# 6: 配置 Nginx ssl

```bash
listen      443;
server_name test.com;

ssl on;
ssl_certificate  /etc/tls/server.crt; #server端公钥
ssl_certificate_key  /etc/tls/server.key; #server端私钥
ssl_client_certificate  /etc/tls/client.crt; #client端公钥
ssl_password_file /etc/tls/passphrase;
ssl_session_timeout 5m;

# This is important to enforce client to use certificate.
# The client of nginx cannot use a self-signed cert.
ssl_verify_client on; #开启client验证
ssl_client_certificate /tmp/nginx/ca.crt;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
ssl_prefer_server_ciphers on;
ssl_ciphers ECDH+AES256:ECDH+AES128:DH+3DES:!ADH:!AECDH:!MD5@SECLEVEL=1;
```
