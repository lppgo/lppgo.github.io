---
title: "041-Linux systemd & journalctl"
author: "lucas"
date: 2025-12-13
lastmod: 2025-12-13

tags: ["Linux"]
categories: ["Linux"]
keywords: ["systemd","systemd", "journalctl"]
---

- [1: 使用 systemd 管理服务](#1-使用-systemd-管理服务)
  - [1.1 systemd 介绍](#11-systemd-介绍)
  - [1.2 systemd 服务文件配置](#12-systemd-服务文件配置)
  - [1.3 systemd & journalclt 命令汇总](#13-systemd-&-journalclt-命令汇总)
 

# 1: 使用 systemd 管理服务
## 1.1 systemd 介绍
- systemctl是Linux中管理systemd服务的核心工具，通过统一命令集实现服务启动、停止、重启、状态查看及开机自启设置，支持并行启动、依赖管理与日志集中查看，显著提升服务管理效率
## 1.2 systemd 服务文件配置
```bash 
# /etc/systemd/system/app.service # xxx.ini格式
#
[Unit]
Description=My Custom Service         # 服务描述
Documentation=https://your-docs-link.com (可选)
After=network.target                  # 服务启动顺序（在 network.target 之后启动）
Requires=network-online.target        # 强制依赖（服务启动前必须满足）
Wants=another-service.target          # 弱依赖（服务启动前尝试启动 another-service）
Conflicts=httpd.service               # 冲突服务（与 httpd 互斥）
————————————————
版权声明：本文为CSDN博主「岚叔运维」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lmzf2011/article/details/150656143
[Service]
Type=simple # [simple, forking, oneshot, notify, dbus, idle]
User=gitlab
Group=gitlab
WorkingDirectory=/opt/gitlab/bin/
ExecStart=/opt/gitlab/bin/gitlab-ctl start  # 必须使用绝对路径来指定启动命令或脚本
ExecStop=/opt/gitlab/bin/gitlab-ctl stop
Restart=on-failure # [no,on-failure,on-abnormal,alaways]
RestartSec=5s
Environment=NODE_ENV=production # 直接设置环境变量
EnvironmentFile=/home/proj/app/config # 从指定文件加载环境变量，格式为 KEY=VAL，适合配置较多的情况
LimitNOFILE=65536 # 限制打开的文件数
LimitCPU=500% # 限制CPU使用率,infinity表示无限制
MemoryMax=8G

[Install]
WantedBy=multi-user.target # 表示当系统进入“多用户命令行模式”（标准服务器运行级别）时，该服务应被自动启动。这是实现开机自启的关键
```
## 1.3 systemd & journalclt 命令汇总
```bash
sudo apt install systemd # install 

sudo systemctl status gitlab # status
sudo systemctl start gitlab  # start service
sudo systemctl stop gitlab   # stop
sudo systemctl restart gitlab # restart
sudo systemctl enable gitlab  # enable 服务开机自启
sudo systemctl disable gitlab # disable 禁止服务开机自启
sudo systemctl reload gitlab # 优雅的重载gitlab配置

sudo systemctl daemon-reload # 重新加载systemd配置
sudo systemctl list-units --type=service  # 查看所有服务单元
sudo systemctl list-units --type=service --state=active # 查看所有活跃的服务单元
sudo systemctl list-units --type=service --state=inactive # 查看所有不活跃的服务单元
sudo systemctl list-units --type=service --state=failed # 查看所有失败的服务单元
sudo systemctl --failed  #查看失败的服务


sudo journalctl -u gitlab  # 查看gitlab日志
sudo journalctl -u gitlab -f # 查看gitlab日志，实时更新
sudo journalctl -u gitlab --since "1 hour ago" # 查看gitlab日志，最近一小时
sudo journalctl -b -u your-app.service # 查看your-app.service日志，最近一次启动
sudo journalctl -u your-app.service --since "2024-06-13 09:00:00" --until "2024-06-13 10:00:00"  # 按照时间范围查看your-app.service日志
sudo journalctl -p err -u your-app.service # 按日志级别过滤, 只显示错误级别（ERROR）及以上的日志，帮助快速定位问题


# 管理 journald 系统日志
journalctl --disk-usage # 检查当前日志占用的磁盘空间
sudo journalctl --vacuum-time=7d  # 清理日志，保留最近7天的日志
sudo journalctl --vacuum-size=100M # 清理日志，保留100M大小的日志
sudo journalctl --vacuum-files=10 # 清理日志，保留最近10个日志文件
sudo journalctl --vacuum-files=10 --vacuum-time=7d --vacuum-size=100M # 清理日志，保留最近10个日志文件，最近7天的日志，100M大小的日志

# 永久性配置：若要一劳永逸，可以编辑 /etc/systemd/journald.conf文件，设置限制
#  [Journal]
# SystemMaxUse=1G
# MaxRetentionSec=1week
# 运行 sudo systemctl restart systemd-journald 使配置生效

```
