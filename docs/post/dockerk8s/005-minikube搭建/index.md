
[toc]

# 1: 安装 Docker 环境

## 1.1: 安装 docker

## 1.2: 配置 docker

docker 加速 `/etc/docker/daemon.json`
重启 docker,使配置生效

```bash
sudo systemctl daemon-reload

sudo systemctl restart docker
```

# 2: 安装 Minikube

https://cloud.tencent.com/developer/article/1817826

## 2.1 使用普通的 minikube

### 2.1.1 更新软件源

### 2.1.2 更新软件包

### 2.1.3 安装 docker

### 2.1.4 安装 k8s

```bash
# 执行以下命令安装 https 工具以及 k8s
apt-get update && apt-get install -y apt-transport-https curl
apt-get install -y kubelet kubeadm kubectl --allow-unauthenticated

# 执行下面命令测试是否正常
kubeadm init

# 如果安装时，出现下面情况，说明系统得镜像源中，找不到 k8s 的软件包
No apt package "kubeadm", but there is a snap with that name.
Try "snap install kubeadm"

No apt package "kubectl", but there is a snap with that name.
Try "snap install kubectl"

# 可以打开 /etc/apt/sources.list  文件，添加一行
deb https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial main

# 再次执行安装k8s

# 如果出现下面
The following signatures couldn't be verified because the public key is not available

# 则执行下面命令，添加key
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add
```

> 上面命令，安装了 `kubelet`、`kubeadm`、`kubectl`
>
> kubelet 是 k8s 相关服务，
> kubectl 是 k8s 管理客户端，
> kubeadm 是部署工具

## 2.2 使用 aliyun 的 minikube

https://developer.aliyun.com/article/221687

1. 安装 aliyun minikube

```bash
curl -Lo minikube https://kubernetes.oss-cn-hangzhou.aliyuncs.com/minikube/releases/v1.18.1/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

2. minikube 基本命令

```bash
# 启动
minikube start --driver=docker

# 查看状态status
minikube status

# 打开dashboard
 minikube dashboard
```

# 1: Nginx
