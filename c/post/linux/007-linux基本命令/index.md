
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
  - [13.1 dpkg - (Ubuntu,Debian)](#131-dpkg---ubuntudebian)
  - [13.2 apt - (Ubuntu,Debian)](#132-apt---ubuntudebian)
  - [13.3 rpm -（RHEL, CentOS 及类似系统）](#133-rpm--rhel-centos-及类似系统)
  - [13.4 yum -（Fedora, RedHat,CentOS 及类似系统）](#134-yum--fedora-redhatcentos-及类似系统)
  - [13.5 dnf -（RHEL8、CentOS8）](#135-dnf--rhel8centos8)
- [14: 常用命令](#14-常用命令)
  - [14.1 查看端口的占用](#141-查看端口的占用)
  - [14.2 查看进程](#142-查看进程)
  - [14.3 批量杀死进程](#143-批量杀死进程)
  - [14.4 查看当前时间](#144-查看当前时间)
  - [14.5 查看进程内存使用情况](#145-查看进程内存使用情况)
  - [14.5 查看 Linux 内核版本或发布版本](#145-查看-linux-内核版本或发布版本)
  - [14.6 查看本地网络服务活动状态](#146-查看本地网络服务活动状态)
  - [14.7 查看自己的外网 ip](#147-查看自己的外网-ip)
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

> 介绍常见 Linux 操作系统的安装包管理工具，主要介绍其使用命令.

## 13.1 dpkg - (Ubuntu,Debian)

- dpkg 命令是 Debian Linux 系统用来安装、创建和管理软件包的实用工具
- **命令行使用**

```bash
# -------------------dpkg(选项)(参数)---------------------
$ dpkg --help
Usage: dpkg [<option> ...] <command>

# 选项
-i：安装软件包
-r：删除软件包
-P：删除软件包的同时删除其配置文件
-L：显示于软件包关联的文件
-l：显示已安装软件包列表
--unpack：解开软件包
-c：显示软件包内文件列表
--confiugre：配置软件包

# 参数
Deb软件包：指定要操作的.deb软件包
```

- **示例演示说明**

```bash
# -------------------示例演示说明---------------------
# 安装包
$ dpkg -i package.deb
# 删除包
$ dpkg -r package
# 删除包（包括配置文件）
$ dpkg -P package
# 列出与该包关联的文件
$ dpkg -L package
# 显示该包的版本
$ dpkg -l package
# 解开deb包的内容
$ dpkg --unpack package.deb
# 搜索所属的包内容
$ dpkg -S keyword
# 列出当前已安装的包
$ dpkg -l
# 列出deb包的内容
$ dpkg -c package.deb
# 配置包
$ dpkg --configure package

# 列出已安装软件包
$ sudo dpkg-query -l
$ sudo dpkg-query -l | less
$ sudo dpkg-query -l | grep tmux
```

## 13.2 apt - (Ubuntu,Debian)

- apt-get 命令是 Debian Linux 发行版中的 APT 软件包管理工具。所有基于 Debian 的发行都使用这个包管理系统。deb 包可以把一个应用的文件包在一起，大体就如同 Windows 上的安装文件.
- **命令行使用**

```bash
# apt-get(选项)(参数)
$ apt --help
Usage: apt [options] command

# 选项
-c：指定配置文件

# 参数
管理指令：对APT软件包的管理操作
软件包：指定要操纵的软件包
```

- **示例演示说明**

```bash
# 更新所有已安装的软件包
$ apt-get upgrade
# 将系统升级到新版本
$ apt-get dist-upgrade
# 更新
$ apt-get update
# 安装一个新软件包
$ apt-get install packagename
# 卸载一个已安装的软件包（保留配置文件）
$ apt-get remove packagename
# 卸载一个已安装的软件包（删除配置文件）
$ apt-get –purge remove packagename
# 来删除你已经删掉的软件
$ apt-get autoclean apt
# 会把安装的软件的备份也删除
$ apt-get clean

# 列出已安装软件包
$ sudo apt list --installed
$ sudo apt list --installed | less
$ sudo apt list --installed | grep tmux
```

## 13.3 rpm -（RHEL, CentOS 及类似系统）

- rpm 命令是 RPM 软件包的管理工具。rpm 原本是 Red Hat Linux 发行版专门用来管理 Linux 各项套件的程序，由于它遵循 GPL 规则且功能强大方便，因而广受欢迎。逐渐受到其他发行版的采用。RPM 套件管理方式的出现，让 Linux 易于安装，升级，间接提升了 Linux 的适用度。
- **命令行使用**

```bash
# yum(选项)(参数)
$ yum --help
Loaded plugins: fastestmirror, langpacks
Usage: yum [options] COMMAND

# 选项
-h：显示帮助信息；
-y：对所有的提问都回答“yes”；
-c：指定配置文件；
-q：安静模式；
-v：详细模式；
-d：设置调试等级（0-10）；
-e：设置错误等级（0-10）；
-R：设置yum处理一个命令的最大等待时间；
-C：完全从缓存中运行，而不去下载或者更新任何头文件。

# 参数
install：安装rpm软件包；
update：更新rpm软件包；
check-update：检查是否有可用的更新rpm软件包；
remove：删除指定的rpm软件包；
list：显示软件包的信息；
search：检查软件包的信息；
info：显示指定的rpm软件包的描述信息和概要信息；
clean：清理yum过期的缓存；
shell：进入yum的shell提示符；
resolvedep：显示rpm软件包的依赖关系；
localinstall：安装本地的rpm软件包；
localupdate：显示本地rpm软件包进行更新；
deplist：显示rpm软件包的所有依赖关系。
```

- **示例演示说明**

```shell
rpm -ivh package.rpm 安装一个rpm包 
rpm --force -ivh your-package.rpm 强制安装
rpm -ivh --nodeeps package.rpm 安装一个rpm包而忽略依赖关系警告 
rpm -U package.rpm 更新一个rpm包但不改变其配置文件 
rpm -F package.rpm 更新一个确定已经安装的rpm包 
rpm -e package_name.rpm 卸载一个rpm包 
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
# rpm包中的文件安装到那里
$ rpm -ql ***.rpm
# 一个没有安装过的软件包
$ rpm -qlp ***.rpm
# 一个已经安装过的软件包
$ rpm -ql ***.rpm
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

## 13.4 yum -（Fedora, RedHat,CentOS 及类似系统）

- yum 命令是在 Fedora 和 RedHat 以及 SUSE 中基于 rpm 的软件包管理器，它可以使系统管理人员交互和自动化地更新与管理 RPM 软件包，能够从指定的服务器自动下载 RPM 包并且安装，可以自动处理依赖性关系，并且一次安装所有依赖的软体包，无须繁琐地一次次下载、安装。
- **命令行使用**

```shell
# yum(选项)(参数)
$ yum --help
Loaded plugins: fastestmirror, langpacks
Usage: yum [options] COMMAND

# 选项
-h：显示帮助信息；
-y：对所有的提问都回答“yes”；
-c：指定配置文件；
-q：安静模式；
-v：详细模式；
-d：设置调试等级（0-10）；
-e：设置错误等级（0-10）；
-R：设置yum处理一个命令的最大等待时间；
-C：完全从缓存中运行，而不去下载或者更新任何头文件。

# 参数
install：安装rpm软件包；
update：更新rpm软件包；
check-update：检查是否有可用的更新rpm软件包；
remove：删除指定的rpm软件包；
list：显示软件包的信息；
search：检查软件包的信息；
info：显示指定的rpm软件包的描述信息和概要信息；
clean：清理yum过期的缓存；
shell：进入yum的shell提示符；
resolvedep：显示rpm软件包的依赖关系；
localinstall：安装本地的rpm软件包；
localupdate：显示本地rpm软件包进行更新；
deplist：显示rpm软件包的所有依赖关系。
```

- **示例演示说明**

```bash
# 安装
$ yum install             # 全部安装
$ yum install package1    # 安装指定的安装包package1
$ yum groupinsall group1  # 安装程序组group1

# 更新和升级
$ yum update              # 全部更新
$ yum update package1     # 更新指定程序包package1
$ yum check-update        # 检查可更新的程序
$ yum upgrade package1    # 升级指定程序包package1
$ yum groupupdate group1  # 升级程序组group1

# 查找显示
$ yum list installed | grep mysql
$ yum list installed mysql*
$ yum info package1     # 显示安装包信息package1
$ yum list              # 显示所有已经安装和可以安装的程序包
$ yum list package1     # 显示指定程序包安装情况package1
$ yum groupinfo group1  # 显示程序组group1信息

# 删除程序
$ yum remove/erase package1  # 删除程序包package1
$ yum groupremove group1     # 删除程序组group1
$ yum deplist package1       # 查看程序package1依赖情况

# 清除缓存
$ yum clean packages    # 清除缓存目录下的软件包
$ yum clean headers     # 清除缓存目录下的 headers
$ yum clean oldheaders  # 清除缓存目录下旧的 headers
```

## 13.5 dnf -（RHEL8、CentOS8）

- DNF 使用 libsolv 进行依赖解析，由 SUSE 开发和维护，旨在提高性能。Yum 主要是用 Python 编写的，它有自己的应对依赖解析的方法。它的 API 没有完整的文档，它的扩展系统只允许 Python 插件。Yum 是 RPM 的前端工具，它管理依赖关系和资源库，然后使用 RPM 来安装、下载和删除包。

- 由于 Yum 中许多长期存在的问题仍未得到解决，因此 Yum 包管理器已被 DNF 包管理器取代。这些问题包括性能差、内存占用过多、依赖解析速度变慢等。两个管理包工具的更多区别可以查看，What is the difference between DNF and YUM? 进行阅读。

- **安装 DNF 包管理器**

```bash
# 依赖
$ yum install -y epel-release
# 安装
$ yum install -y dnf
# 检查
$ dnf –version
```

- **常用命令介绍**

```bash
# 安装软件包
$ dnf install nano
# 升级软件包
$ dnf update systemd
# 升级所有系统软件包
$ dnf update
$ dnf upgrade
# 检查系统软件包的更新
$ dnf check-update
# 删除软件包
$ dnf remove nano
$ dnf erase nano
# 删除无用孤立的软件包
$ dnf autoremove
# 删除缓存的无用软件包
$ dnf clean all
# 查看系统中可用的DNF软件库
$ dnf repolist
# 查看系统中可用和不可用的所有的DNF软件库
$ dnf repolist all
# 列出所有RPM包
$ dnf list
# 列出所有安装了的RPM包
$ dnf list installed
# 列出所有可供安装的RPM包
$ dnf list available
# 搜索软件库中的RPM包
$ dnf search nano
# 查找某一文件的提供者
$ dnf provides /bin/bash
# 查看软件包详情
$ dnf info nano
# 查看所有的软件包组
$ dnf grouplist
# 安装一个软件包组
$ dnf groupinstall 'Educational Software'
# 升级一个软件包组中的软件包
$ dnf groupupdate 'Educational Software'
# 删除一个软件包组
$ dnf groupremove 'Educational Software'
# 重新安装特定软件包
$ dnf reinstall nano
# 回滚某个特定软件的版本
$ dnf downgrade acpid
# 查看DNF命令的执行历史
$ dnf history
# 查看所有的DNF命令及其用途
$ dnf help
# 获取有关某条命令的使用帮助
$ dnf help clean
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

## 14.5 查看 Linux 内核版本或发布版本

```bash
lsb_release -a
uname -a
```

## 14.6 查看本地网络服务活动状态

```bash
lsof -i
```

## 14.7 查看自己的外网 ip

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
