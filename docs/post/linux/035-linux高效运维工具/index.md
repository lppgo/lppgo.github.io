
[toc]

<div align="center"><font size="35">Linux高效运维工具</font></div>

- [1: 系统性能，资源](#1-系统性能资源)
  - [1.1 top](#11-top)
  - [1.2 htop](#12-htop)
  - [1.3 btop/gotop](#13-btopgotop)
  - [1.4 系统资源监控-NMON](#14-系统资源监控-nmon)
- [2: 网络 Network](#2-网络-network)
  - [2.1 网络流量监控 iftop](#21-网络流量监控-iftop)
  - [2.2 查看进程占用带宽情况 nethogs](#22-查看进程占用带宽情况-nethogs)
  - [2.3 网络流量监控 IPtraf](#23-网络流量监控-iptraf)
- [3: 磁盘](#3-磁盘)
  - [3.1 硬盘读取性能测试 iozone](#31-硬盘读取性能测试-iozone)
  - [3.2 实时监控磁盘 IO ioTop](#32-实时监控磁盘-io-iotop)
  - [3.3 页面显示磁盘空间使用情况-Agedu](#33-页面显示磁盘空间使用情况-agedu)
  - [3.4 iostat](#34-iostat)
- [4: 进程监控](#4-进程监控)
- [5: Container](#5-container)
- [6: 安全扫描](#6-安全扫描)
  - [6.1 安全扫描工具-NMap](#61-安全扫描工具-nmap)
- [7: web](#7-web)
- [7.1 Web 压力测试-Httperf](#71-web-压力测试-httperf)
- [8: 文件监控](#8-文件监控)
  - [8.1 监控多个日志-MultiTail](#81-监控多个日志-multitail)
  - [8.2 页面显示磁盘空间使用情况-Agedu](#82-页面显示磁盘空间使用情况-agedu)
- [9: 会话 Session 终端](#9-会话-session-终端)
  - [9.1 连接会话终端持续化-Tmux](#91-连接会话终端持续化-tmux)

---

# 1: 系统性能，资源

## 1.1 top

## 1.2 htop

- `yum -y install htop`

## 1.3 btop/gotop

## 1.4 系统资源监控-NMON

> NMON 是一种在 AIX 与各种 Linux 操作系统上广泛使用的监控与分析工具.

- `apt install -y nmon`

# 2: 网络 Network

## 2.1 网络流量监控 iftop

- **install:** `sudo apt install iftop`
- **Usage:**

```go
iftop -i eth0 -B

// TX：发送流量
// RX：接收流量
// TOTAL：总流量
// Cumm：运行iftop到目前时间的总流量
// peak：流量峰值
// rates：分别表示过去 2s 10s 40s 的平均流量
```

## 2.2 查看进程占用带宽情况 nethogs

- **install:** `sudo apt install nethogs -y`
- **Usage:**

```go
nethogs eth0 // 指定某个网卡
nethogs -d 1 //设置刷新频率

// 交互模式，在进入 nethogs 之后，可以使用如下的交互命令:
m: 修改网速单位
r: 按照流量排序
s: 按照发送流量排序
q: 退出
```

## 2.3 网络流量监控 IPtraf

> IPtraf 是一个运行在 Linux 下的简单的网络状况分析工具.

- **install:** `yum -y install iptraf`
- **Usage:**

```bash

```

# 3: 磁盘

## 3.1 硬盘读取性能测试 iozone

- **install:** `sudo apt install nethogs -y`
- **Usage:**

```bash
iozone -a -i 0 -i 1 -i 2 -f /home/hdd/testfile -r 16m -s 8G | tee -a iozone1.log
# #设置大小为物理内存的一半；存放到iozone1.log下查看
tee 命令
iozone -a -n 512m -g 16g -i 0 -i 1 -i 5 -f /mnt/iozone -Rb ./iozone.xls

-a使用全自动模式
-n为自动模式设置最小文件大小(Kbytes)。
-g设置自动模式可使用的最大文件大小Kbytes。
-i用来指定运行哪个测试。
-f指定测试文件的名字完成后自动删除
-R产生Excel到标准输出
-b指定输出到指定文件上
# ------ 备注：各参数的含义 ------
-a #使用全自动模式
-i #指定运行于哪种模式测试。可以使用-i # -i # -i #进行多个测试
0=write/rewrite
1=read/re-read
2=random read/random write
-f #指定用来测试的临时文件，测试完后会自动删除
-r #设置测试文件的块大小
-s #设置测试文件的大小，要求为物理内存的1/2，1倍，2倍
-I #直接IO，可排除掉缓存的影响，直接对硬盘读写
```

- https://blog.csdn.net/weixin_42480467/article/details/121744677

## 3.2 实时监控磁盘 IO ioTop

> IOTop 命令是专门显示硬盘 IO 的命令,界面风格类似 top 命令.

- **install:** `yum -y install iotop`
- **Usage:**

```bash

```

## 3.3 页面显示磁盘空间使用情况-Agedu

- **install:** `yum -y install iotop`
- **Usage:**

```bash

```

- https://blog.csdn.net/carefree2005/article/details/124254821

## 3.4 iostat

- **install:** `apt-get install sysstat -y`
- **Usage:**

```bash
iostat -d -k 1 10
Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda              39.29        21.14         1.44  441339807   29990031
sda1              0.00         0.00         0.00       1623        523
sda2              1.32         1.43         4.54   29834273   94827104
sda3              6.30         0.85        24.95   17816289  520725244

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda             327.55      5159.18       102.04       5056        100
sda1              0.00         0.00         0.00          0          0

# 输出信息的意义
tps：该设备每秒的传输次数（Indicate the number of transfers per second that were issued to the device.）。"一次传输"意思是"一次I/O请求"。多个逻辑请求可能会被合并为"一次I/O请求"。"一次传输"请求的大小是未知的。

kB_read/s：每秒从设备（drive expressed）读取的数据量；
kB_wrtn/s：每秒向设备（drive expressed）写入的数据量；
kB_read：读取的总数据量；
kB_wrtn：写入的总数量数据量；这些单位都为Kilobytes。
```

- https://blog.csdn.net/carefree2005/article/details/124254821

# 4: 进程监控

# 5: Container

# 6: 安全扫描

## 6.1 安全扫描工具-NMap

> NMap 是 Linux 下的网络连接扫描和嗅探工具包,用来扫描网上电脑开放的网络连接端。

- **install:** `yum -y install nmap`;
- **Usage:**

```bash

```

- https://www.cnblogs.com/gxn8638/p/16274195.html

# 7: web

# 7.1 Web 压力测试-Httperf

> Httperf 比 ab 更强大，能测试出 web 服务能承载的最大服务量及发现潜在问题；比如：内存使用、稳定性。最大优势：可以指定规律进行压力测试，模拟真实环境。

- **install:** `yum -y install multitail`,`apt -y install multitail`;
- **Usage:**

```bash

```

- https://www.cnblogs.com/wangguishe/p/15264244.html

# 8: 文件监控

## 8.1 监控多个日志-MultiTail

> MultiTail 是个用来实现同时监控多个文档、类似 tail 命令的功能的软件.

- **install:** `yum -y install multitail`,`apt -y install multitail`;
- **Usage:**

```bash

```

- https://www.cnblogs.com/wangguishe/p/15264244.html

## 8.2 页面显示磁盘空间使用情况-Agedu

- **install:** `yum install -y agedu`;
- **Usage:**

```bash
$ agedu -s / -w --address 0.0.0.0:9999 --auth basic
Built pathname index, 453297 entries, 40723929 bytes of index
Faking directory atimes
Building index
Final index file size = 149385592 bytes
Username: agedu
Password: 0h9bbda14yg532rh
URL: http://iZf8z3ylerfr8lt1be68xpZ:9999/

```

- https://blog.csdn.net/carefree2005/article/details/124254821

# 9: 会话 Session 终端

## 9.1 连接会话终端持续化-Tmux

> tmux 是一个可以让人们通过一个窗口操作多个会话的工具.

- **install:** `yum install -y tmux`,`apt-get install tmux`;
- **tmux 应用场景:**

  - 终端长时间连接运行 task，session 断开导致 task 运行失败;也可以用 nohup xxx \*;
  - 多窗口切换;
  - 一屏显示多窗口;

- **Usage:**

```bash

# ----------session-----------
tmux new -s lpp # 创建一个新的session,同时会创建一个windows 0:bash
tmux detach -s lpp # tmux与当前 lpp session 分离，lpp session进入后台
快捷键[ctrb+b , d]  # tmux与当前 lpp session 分离，lpp session进入后台
# tmux与当前 lpp session 分离，lpp session进入后台
tmux ls # 查看已创建的后台sessions

tmux attach -t lpp # 重新接入已创建的会话lpp session
tmux a      -t lpp # 重新接入已创建的会话lpp session,简写



# ----------windows-----------
# 星号（*）在这里表示的是“当前处于活跃状态的窗口”;
ctrl + b 组合键，松开后再按c; # 创建一个新窗口, 1:bash
ctrl + b 组合键，松开后再按0; # 切换到窗口0
# 给新建的窗口重命名
先按Ctrl+b之后再按 : , 输入命名： rename-window [窗口名字]

ctrl + d ，kill 当前session的swindows;# kill 0 bash之后只剩1了
ctrl + d # 当把当前的session的所有窗口都kill之后，session也就被kill了

# --------------------------------
命令：
tmux 启动tmux
tmux a 恢复最近关闭会话
tmux ls 查看所有会话


常用快捷键：

Ctrl+b,c（按Ctrl+b，放开后马上按c） 创建新窗口

Ctrl+b,, 重命名当前窗口

Ctrl+b,p 前一个窗口

Ctrl+b,n 后一个窗口
Ctrl+b,w 选择窗口

Ctrl+b,& 关掉当前窗口

Ctrl+b,d 离开当前会话 

Ctrl+b,% 分成左右两个窗格
Ctrl+b," 分成上下两个窗格
Ctrl+b,方向键 光标移到窗格
Ctrl+b,x 关闭当前窗格

```

![tmux快捷键1](/images/tmux快捷键_001.png)
![tmux快捷键2](/images/tmux快捷键_002.png)
