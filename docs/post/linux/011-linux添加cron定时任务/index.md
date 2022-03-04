
- [1: 安装 Cron](#1-安装-cron)
  - [1.1 Ubuntu 下 crontab 的安装和使用](#11-ubuntu-下-crontab-的安装和使用)
- [2: cron 使用](#2-cron-使用)
  - [2.1: cron 基本命令](#21-cron-基本命令)
  - [2.2: cron 定时任务脚本格式](#22-cron-定时任务脚本格式)
  - [2.3: 对 Cron 任务进行列表显示](#23-对-cron-任务进行列表显示)
  - [2.2: 编辑 cron 定时任务脚本](#22-编辑-cron-定时任务脚本)
  - [2.4 sudo用户编辑/etc/crontab](#24-sudo用户编辑etccrontab)
  - [2.5 restart cron](#25-restart-cron)
- [3: 一些实例](#3-一些实例)
- [4: 一些工具](#4-一些工具)
  - [4.1 在线crontab服务](#41-在线crontab服务)

# 1: 安装 Cron

## 1.1 Ubuntu 下 crontab 的安装和使用

crontab 命令常见于 Unix 和 Linux 的操作系统之中，用于设置周期性被执行的指令。该命令从标准输入设备读取指令，并将其存放于“crontab”文件中，以供之后读取和执行。通常，crontab 储存的指令被守护进程激活。crond 常常在后台运行，每一分钟检查是否有预定的作业需要执行。这类作业一般称为 cron jobs。

```shell
apt install cron
crontab -l # 检查Cronta工具是否安装
service cron start
service cron restart
service cron reload # 重新加载配置
service cron stop
service cron status # 检查状态
service cron # 查询cron可用的命令

# 
systemctl start crond   # 
systemctl stop crond    #
systemctl restart crond #
systemctl reload crond  # 重新加载配置
systemctl status crond  # 查看服务状态
```

# 2: cron 使用

## 2.1: cron 基本命令

```shell
$ service cron
 * Usage: /etc/init.d/cron {start|stop|status|restart|reload|force-reload}
```

## 2.2: cron 定时任务脚本格式

**crontab 文件格式：**

```shell
*   *   *    *    *      command
分  时  日    月   周（几）   命令
```

**特殊字符:**

> 星号（_）：代表’‘每’'的意思，例如 month 字段如果是星号，则表示每月都执行该命令。
> 逗号（,）：表示分隔时段的意思，例如，“1,3,5,7,9”。
> 中杠（-）：表示一个时间范围，例如“2-6”表示“2,3,4,5,6”。
> 正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如_/10，如果用在 minute 字段，表示每十分钟执行一次。

## 2.3: 对 Cron 任务进行列表显示

```shell
# 展示当前user任务列表
crontab -l

# 展示指定user crontab任务列表
crontab -l -u username
```

## 2.2: 编辑 cron 定时任务脚本

```shell
$ crontab -e

*/1 * * * *  /home/lucas/test.sh >> /home/lucas/test.log

# 保存退出

crontab: installing new crontab # 表示创建成功

# 查看脚本
/var/spool/cron

crontab -l

```

## 2.4 sudo用户编辑/etc/crontab
```bash
# 多个用户使用统一的crontab文件
sudo vi /etc/crontab

```
## 2.5 restart cron

```bash
# 重启服务，使配置立即生效
sudo service cron restart
sudo service cron status

sudo systemctl restart crond
sudo systemctl status crond
```

# 3: 一些实例

```go
每月每天凌晨3点30分和中午12点20分执行test.sh脚本
30 3,12 * * * /root/test.sh >> /root/test.log

每月每天每隔6小时的每30分钟执行test.sh脚本
30 */6 * * * /root/test.sh >> /root/test.log

每月每天早上8点到下午18点每隔2小时的每30分钟执行test.sh脚本
30 8-18/2 * * * /root/test.sh >> /root/test.log

每月每天晚上21点30分执行test.sh脚本
30 21 * * * /root/test.sh >> /root/test.log

每月1号、10号、22号凌晨4点45分执行test.sh脚本
45 4 1,10,22 * * /root/test.sh >> /root/test.log

8月份周一、周日凌晨1点10分执行test.sh脚本
10 1 * 8 6,0 /root/test.sh >> /root/test.log

每月每天每小时整点执行test.sh脚本
00 */1 * * * /root/test.sh >> /root/test.log

```

[转]

# 4: 一些工具
## 4.1 在线crontab服务
> crontab表达式生成，在线检查cron的状态
https://crontab.guru/

