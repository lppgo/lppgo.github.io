---
title: "05-Linux基本命令"
author: "lucas" # 文章作者
description: "..."
date: 2021-04-15
lastmod: 2021-04-26

tags: # 文章所属标签
  ["Linux"]
categories: # 文章所属目录
  ["Linux"]
keywords: # 文章关键词
  ["Linux", "tool"]
# prev: ./20210415-04.md # 上一篇博客地址
# next: ./20210416-01.md # 下一篇博客地址
---

- [1: 系统的关机、重启以及登出](#1-系统的关机重启以及登出)
- [2: 文件和目录](#2-文件和目录)
- [3: Linux 查看磁盘 io 的几种方法](#3-linux-查看磁盘-io-的几种方法)
- [4: 查看网卡流量方法](#4-查看网卡流量方法)
- [5: 使用 watch 命令，配合 ifconfig、more /proc/net/dev、cat /proc/net/dev 来实时监控系统信息](#5-使用-watch-命令配合-ifconfigmore-procnetdevcat-procnetdev-来实时监控系统信息)
- [6: 文件搜索](#6-文件搜索)
- [7: 磁盘空间](#7-磁盘空间)
- [8: 用户和群组](#8-用户和群组)
- [9: 文件的权限 - 使用 "+" 设置权限，使用 "-" 用于取消](#9-文件的权限---使用--设置权限使用---用于取消)
- [10: 文件的特殊属性 - 使用 "+" 设置权限，使用 "-" 用于取消](#10-文件的特殊属性---使用--设置权限使用---用于取消)
- [11: 打包和压缩文件](#11-打包和压缩文件)
- [12: 查看文件内容](#12-查看文件内容)
- [13: Linux 包管理器](#13-linux-包管理器)
  - [13.1 RPM -（Fedora, Redhat 及类似系统）](#131-rpm--fedora-redhat-及类似系统)
  - [13.2 YUM -（Fedora, RedHat 及类似系统）](#132-yum--fedora-redhat-及类似系统)
  - [13.2 DEB -（Fedora, RedHat 及类似系统）](#132-deb--fedora-redhat-及类似系统)
  - [13.3 APT - (Debian, Ubuntu 以及类似系统)](#133-apt---debian-ubuntu-以及类似系统)
- [14: 常用命令](#14-常用命令)
  - [14.1 查看端口的占用](#141-查看端口的占用)
  - [14.2 查看进程](#142-查看进程)
  - [14.3 批量杀死进程](#143-批量杀死进程)
  - [14.4 查看当前时间](#144-查看当前时间)
  - [14.5 查看进程内存使用情况](#145-查看进程内存使用情况)
  - [14.5 查看Linux内核版本或发布版本](#145-查看linux内核版本或发布版本)
  - [14.6 查看本地网络服务活动状态](#146-查看本地网络服务活动状态)
  - [14.7 查看自己的外网ip](#147-查看自己的外网ip)
  - [14.8 查看当前文件夹下文件（文件夹）大小](#148-查看当前文件夹下文件文件夹大小)
  - [14.9 查看所有磁盘大小](#149-查看所有磁盘大小)
  - [14.10 诊断网络](#1410-诊断网络)
  - [14.11 列出本机监听的端口号](#1411-列出本机监听的端口号)
  - [14.12 在远程机器上运行一段脚本](#1412-在远程机器上运行一段脚本)
  - [14.13 端口扫描](#1413-端口扫描)

# 1: 系统的关机、重启以及登出

```shell
shutdown -h now # 关闭系统(1) 
init 0 关闭系统(2) 
telinit 0 关闭系统(3) 
shutdown -h hours:minutes & # 按预定时间关闭系统 
shutdown -c # 取消按预定时间关闭系统 
shutdown -r now # 重启(1) 
reboot # 重启(2) 
logout # 注销 
```

# 2: 文件和目录

```shell
cd /home # 进入 '/ home' 目录' 
cd .. # 返回上一级目录 
cd ../.. # 返回上两级目录 
cd - # 返回上次所在的目录 
pwd # 显示工作路径 
ls # 查看目录中的文件 
ls -F # 查看目录中的文件 
ls -l # 显示文件和目录的详细资料 
ls -a # 显示隐藏文件 
ls *[0-9]* # 显示包含数字的文件名和目录名 
tree # 显示文件和目录由根目录开始的树形结构(1) 
lstree # 显示文件和目录由根目录开始的树形结构(2) 
mkdir dir1 dir2 # 同时创建两个目录 
mkdir -p /tmp/dir1/dir2 # 创建一个目录树 
rm -f file1 # 删除一个叫做 'file1' 的文件' 
rmdir dir1 # 删除一个叫做 'dir1' 的目录' 
rm -rf dir1 # 删除一个叫做 'dir1' 的目录并同时删除其内容 
rm -rf dir1 dir2 同时删除两个目录及它们的内容 
mv dir1 new_dir 重命名/移动 一个目录 
cp file1 file2 复制一个文件 
cp dir/* . 复制一个目录下的所有文件到当前工作目录 
cp -a /tmp/dir1 . 复制一个目录到当前工作目录 
cp -a dir1 dir2 复制一个目录 
ln -s file1 lnk1 创建一个指向文件或目录的软链接 
ln file1 lnk1 创建一个指向文件或目录的物理链接 
touch -t 0712250000 file1 修改一个文件或目录的时间戳 - (YYMMDDhhmm) 
file file1 outputs the mime type of the file as text 
iconv -l 列出已知的编码 
iconv -f fromEncoding -t toEncoding inputFile > outputFile creates a new from the given input file by assuming it is encoded in fromEncoding and converting it to toEncoding. 
find . -maxdepth 1 -name *.jpg -print -exec convert "{}" -resize 80x60 "thumbs/{}" \; batch resize files in the current directory and send them to a thumbnails directory (requires convert from Imagemagick) 
```

# 3: Linux 查看磁盘 io 的几种方法

```shell
1. 用 top 命令 中的cpu 信息观察. (还有htop,gotop)

2. vmstat：vmstat 命令报告关于线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息

3. iostat

4. iotop

5. sar -d
```

# 4: 查看网卡流量方法

```shell
1. sar -n DEV 1 2   （命令后面1 2 意思是：每一秒钟取1次值，取2次。）

2. cat /proc/net/dev

3. iftop

4. ifstat

5. nload

6. gotop
```

# 5: 使用 watch 命令，配合 ifconfig、more /proc/net/dev、cat /proc/net/dev 来实时监控系统信息

```shell
arch # 显示机器的处理器架构(1) 
uname -m # 显示机器的处理器架构(2) 
uname -r # 显示正在使用的内核版本 
dmidecode -q # 显示硬件系统部件 - (SMBIOS / DMI) 
hdparm -i /dev/hda # 罗列一个磁盘的架构特性 
hdparm -tT /dev/sda # 在磁盘上执行测试性读取操作 
cat /proc/cpuinfo # 显示CPU info的信息 
cat /proc/interrupts # 显示中断 
cat /proc/meminfo # 校验内存使用 
cat /proc/swaps # 显示哪些swap被使用 
cat /proc/version # 显示内核的版本 
cat /proc/net/dev # 显示网络适配器及统计 
cat /proc/mounts # 显示已加载的文件系统 
lspci -tv # 罗列 PCI 设备 
lsusb -tv # 显示 USB 设备 
date # 显示系统日期 
cal 2021 # 显示2021年的日历表 
date 041217002007.00 设置日期和时间 - 月日时分年.秒 
clock -w 将时间修改保存到 BIOS 
```

# 6: 文件搜索

```shell
find / -name file1 从 '/' 开始进入根文件系统搜索文件和目录 
find / -user user1 搜索属于用户 'user1' 的文件和目录 
find /home/user1 -name \*.bin 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件 
find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件 
find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件 
find / -name \*.rpm -exec chmod 755 '{}' \; 搜索以 '.rpm' 结尾的文件并定义其权限 
find / -xdev -name \*.rpm 搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备 
locate \*.ps 寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令 
whereis halt 显示一个二进制文件、源码或man的位置 
which halt 显示一个二进制文件或可执行文件的完整路径 
```

# 7: 磁盘空间

```shell
df -h 显示已经挂载的分区列表 
ls -lSr |more 以尺寸大小排列文件和目录 
du -sh dir1 估算目录 'dir1' 已经使用的磁盘空间' 
du -sk * | sort -rn 以容量大小为依据依次显示文件和目录的大小 
rpm -q -a --qf '%10{SIZE}t%{NAME}n' | sort -k1,1n 以大小为依据依次显示已安装的rpm包所使用的空间 (fedora, redhat类系统) 
dpkg-query -W -f='${Installed-Size;10}t${Package}n' | sort -k1,1n 以大小为依据显示已安装的deb包所使用的空间 (ubuntu, debian类系统) 
```

# 8: 用户和群组

```shell
groupadd group_name 创建一个新用户组 
groupdel group_name 删除一个用户组 
groupmod -n new_group_name old_group_name 重命名一个用户组 
useradd -c "Name Surname " -g admin -d /home/user1 -s /bin/bash user1 创建一个属于 "admin" 用户组的用户 
useradd user1 创建一个新用户 
userdel -r user1 删除一个用户 ( '-r' 排除主目录) 
usermod -c "User FTP" -g system -d /ftp/user1 -s /bin/nologin user1 修改用户属性 
passwd 修改口令 
passwd user1 修改一个用户的口令 (只允许root执行) 
chage -E 2005-12-31 user1 设置用户口令的失效期限 
pwck 检查 '/etc/passwd' 的文件格式和语法修正以及存在的用户 
grpck 检查 '/etc/passwd' 的文件格式和语法修正以及存在的群组 
newgrp group_name 登陆进一个新的群组以改变新创建文件的预设群组 
```

# 9: 文件的权限 - 使用 "+" 设置权限，使用 "-" 用于取消

```shell
ls -lh 显示权限 
ls /tmp | pr -T5 -W$COLUMNS 将终端划分成5栏显示 
chmod ugo +rwx directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读（r ）、写(w)和执行(x)的权限 
chmod go -rwx directory1 删除群组(g)与其他人(o)对目录的读写执行权限 
chown user1 file1 改变一个文件的所有人属性 
chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性 
chgrp group1 file1 改变文件的群组 
chown user1:group1 file1 改变一个文件的所有人和群组属性 
find / -perm -u+s 罗列一个系统中所有使用了SUID控制的文件 
chmod u+s /bin/file1 设置一个二进制文件的 SUID 位 - 运行该文件的用户也被赋予和所有者同样的权限 
chmod u-s /bin/file1 禁用一个二进制文件的 SUID位 
chmod g+s /home/public 设置一个目录的SGID 位 - 类似SUID ，不过这是针对目录的 
chmod g-s /home/public 禁用一个目录的 SGID 位 
chmod o+t /home/public 设置一个文件的 STIKY 位 - 只允许合法所有人删除文件 
chmod o-t /home/public 禁用一个目录的 STIKY 位 
```

# 10: 文件的特殊属性 - 使用 "+" 设置权限，使用 "-" 用于取消

```shell
chattr +a file1 只允许以追加方式读写文件 
chattr +c file1 允许这个文件能被内核自动压缩/解压 
chattr +d file1 在进行文件系统备份时，dump程序将忽略这个文件 
chattr +i file1 设置成不可变的文件，不能被删除、修改、重命名或者链接 
chattr +s file1 允许一个文件被安全地删除 
chattr +S file1 一旦应用程序对这个文件执行了写操作，使系统立刻把修改的结果写到磁盘 
chattr +u file1 若文件被删除，系统会允许你在以后恢复这个被删除的文件 
lsattr 显示特殊的属性 
```

# 11: 打包和压缩文件

```shell
bunzip2 file1.bz2 解压一个叫做 'file1.bz2'的文件 
bzip2 file1 压缩一个叫做 'file1' 的文件 
gunzip file1.gz 解压一个叫做 'file1.gz'的文件 
gzip file1 压缩一个叫做 'file1'的文件 
gzip -9 file1 最大程度压缩 
rar a file1.rar test_file 创建一个叫做 'file1.rar' 的包 
rar a file1.rar file1 file2 dir1 同时压缩 'file1', 'file2' 以及目录 'dir1' 
rar x file1.rar 解压rar包 
unrar x file1.rar 解压rar包 
tar -cvf archive.tar file1 创建一个非压缩的 tarball 
tar -cvf archive.tar file1 file2 dir1 创建一个包含了 'file1', 'file2' 以及 'dir1'的档案文件 
tar -tf archive.tar 显示一个包中的内容 
tar -xvf archive.tar 释放一个包 
tar -xvf archive.tar -C /tmp 将压缩包释放到 /tmp目录下 
tar -cvfj archive.tar.bz2 dir1 创建一个bzip2格式的压缩包 
tar -xvfj archive.tar.bz2 解压一个bzip2格式的压缩包 
tar -cvfz archive.tar.gz dir1 创建一个gzip格式的压缩包 
tar -xvfz archive.tar.gz 解压一个gzip格式的压缩包 
zip file1.zip file1 创建一个zip格式的压缩包 
zip -r file1.zip file1 file2 dir1 将几个文件和目录同时压缩成一个zip格式的压缩包 
unzip file1.zip 解压一个zip格式压缩包 
```

# 12: 查看文件内容

```shell
cat file1 从第一个字节开始正向查看文件的内容 
tac file1 从最后一行开始反向查看一个文件的内容 
more file1 查看一个长文件的内容 
less file1 类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作 
head -2 file1 查看一个文件的前两行 
tail -2 file1 查看一个文件的最后两行 
tail -f /var/log/messages 实时查看被添加到一个文件中的内容 
```

# 13: Linux 包管理器

## 13.1 RPM -（Fedora, Redhat 及类似系统）

```shell
rpm -ivh package.rpm 安装一个rpm包 
rpm -ivh --nodeeps package.rpm 安装一个rpm包而忽略依赖关系警告 
rpm -U package.rpm 更新一个rpm包但不改变其配置文件 
rpm -F package.rpm 更新一个确定已经安装的rpm包 
rpm -e package_name.rpm 删除一个rpm包 
rpm -qa 显示系统中所有已经安装的rpm包 
rpm -qa | grep httpd 显示所有名称中包含 "httpd" 字样的rpm包 
rpm -qi package_name 获取一个已安装包的特殊信息 
rpm -qg "System Environment/Daemons" 显示一个组件的rpm包 
rpm -ql package_name 显示一个已经安装的rpm包提供的文件列表 
rpm -qc package_name 显示一个已经安装的rpm包提供的配置文件列表 
rpm -q package_name --whatrequires 显示与一个rpm包存在依赖关系的列表 
rpm -q package_name --whatprovides 显示一个rpm包所占的体积 
rpm -q package_name --scripts 显示在安装/删除期间所执行的脚本l 
rpm -q package_name --changelog 显示一个rpm包的修改历史 
rpm -qf /etc/httpd/conf/httpd.conf 确认所给的文件由哪个rpm包所提供 
rpm -qp package.rpm -l 显示由一个尚未安装的rpm包提供的文件列表 
rpm --import /media/cdrom/RPM-GPG-KEY 导入公钥数字证书 
rpm --checksig package.rpm 确认一个rpm包的完整性 
rpm -qa gpg-pubkey 确认已安装的所有rpm包的完整性 
rpm -V package_name 检查文件尺寸、 许可、类型、所有者、群组、MD5检查以及最后修改时间 
rpm -Va 检查系统中所有已安装的rpm包- 小心使用 
rpm -Vp package.rpm 确认一个rpm包还未安装 
rpm2cpio package.rpm | cpio --extract --make-directories *bin* 从一个rpm包运行可执行文件 
rpm -ivh /usr/src/redhat/RPMS/`arch`/package.rpm 从一个rpm源码安装一个构建好的包 
rpmbuild --rebuild package_name.src.rpm 从一个rpm源码构建一个 rpm 包 
```

## 13.2 YUM -（Fedora, RedHat 及类似系统）

```shell
yum install package_name 下载并安装一个rpm包 
yum localinstall package_name.rpm 将安装一个rpm包，使用你自己的软件仓库为你解决所有依赖关系 
yum update package_name.rpm 更新当前系统中所有安装的rpm包 
yum update package_name 更新一个rpm包 
yum remove package_name 删除一个rpm包 
yum list 列出当前系统中安装的所有包 
yum search package_name 在rpm仓库中搜寻软件包 
yum clean packages 清理rpm缓存删除下载的包 
yum clean headers 删除所有头文件 
yum clean all 删除所有缓存的包和头文件 
```

## 13.2 DEB -（Fedora, RedHat 及类似系统）

```shell
dpkg -i package.deb 安装/更新一个 deb 包 
dpkg -r package_name 从系统删除一个 deb 包 
dpkg -l 显示系统中所有已经安装的 deb 包 
dpkg -l | grep httpd 显示所有名称中包含 "httpd" 字样的deb包 
dpkg -s package_name 获得已经安装在系统中一个特殊包的信息 
dpkg -L package_name 显示系统中已经安装的一个deb包所提供的文件列表 
dpkg --contents package.deb 显示尚未安装的一个包所提供的文件列表 
dpkg -S /bin/ping 确认所给的文件由哪个deb包提供 
```

## 13.3 APT - (Debian, Ubuntu 以及类似系统)

```shell
apt-get install package_name 安装/更新一个 deb 包 
apt-cdrom install package_name 从光盘安装/更新一个 deb 包 
apt-get update 升级列表中的软件包 
apt-get upgrade 升级所有已安装的软件 
apt-get remove package_name 从系统删除一个deb包 
apt-get check 确认依赖的软件仓库正确 
apt-get clean 从下载的软件包中清理缓存 
apt-cache search searched-package 返回包含所要搜索字符串的软件包名称 
```


# 14: 常用命令
## 14.1 查看端口的占用
```bash
lsof -i:8087  # 查看8087端口的使用
```
## 14.2 查看进程
```bash
ps -aux | grep name

# 查看进程执行的时间
ps -A -opid,stime,etime,args | grep python

# 创建守护进程
nohup python /var/www/a.py &
```
## 14.3 批量杀死进程
```bash
ps -aux|grep name|grep -v grep|cut -c 9-15|xargs kill -9
```
## 14.4 查看当前时间
```bash
date       时间
date +%s   时间戳
date -d "2010-07-20 10:25:30" +%s  指定时间时间戳
date -d "@1279592730"    时间戳转时间
date -d "1970-01-01 14781 days" "+%Y/%m/%d %H:%M:%S" 
```
## 14.5 查看进程内存使用情况
```bash
top -d 1 -p pid [,pid ...]
pmap pid 
ps aux|grep process_name
查看/proc/process_id/文件夹下的status文件
```
## 14.5 查看Linux内核版本或发布版本
```bash
lsb_release -a
uname -a
```
## 14.6 查看本地网络服务活动状态
```bash
lsof -i
```
## 14.7 查看自己的外网ip
```bash
curl ifconfig.me
```
## 14.8 查看当前文件夹下文件（文件夹）大小
```bash
du -h --max-depth=1 .
```
## 14.9 查看所有磁盘大小
```bash
df -h
```
## 14.10 诊断网络
```bash
mtr 
ping
traceroute
dig
```
## 14.11 列出本机监听的端口号
```bash
netstat –tlnp
netstat -anop
```
## 14.12 在远程机器上运行一段脚本
```bash
ssh user@server bash < /path/to/local/script.sh
```
## 14.13 端口扫描
```bash
nc -z -v -n 127.0.0.1 20-100
```