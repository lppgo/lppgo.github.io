---
title: "010-update-alternatives安装gcc多版本"
author: "lucas"
date: 2025-03-17
lastmod: 2025-03-17

tags: ["Linux","update-alternatives","多版本","gcc"]
categories: ["C++"]
keywords: ["多版本", "update", "alternatives","update-alternatives","linux"]
---

<div align='center' ><font size='50'>update-alternatives安装gcc多版本</font></div>

# 1: 安装update-alternatives
- 该工具属于dpkg软件包管理系统的核心组件，一般系统已预装。若提示命令不存在，可通过以下命令安装
- 安装: `sudo apt install dpkg`
- 验证: `update-alternatives --help`



# 2: ​添加旧版本软件源（针对gcc-4.8.5）
- 由于Ubuntu 2024.04的默认源可能不包含gcc-4.8.5，需要手动添加旧版仓库: 
```bash
sudo sed -i '$a deb http://archive.ubuntu.com/ubuntu/ xenial main universe' /etc/apt/sources.list
sudo apt update
```

# 3: 安装各版本GCC/G++
```bash
# 安装gcc/g++ 4.8.5（需依赖旧版源）
sudo apt install gcc-4.8 g++-4.8

# 安装gcc/g++ 7和9
sudo apt install gcc-7 g++-7 

#（默认源支持）
sudo apt install gcc-9 g++-9


# 如果apt 安装不了，手动下载安装
https://ftp.gnu.org/gnu/gcc/
```

# 4: 配置update-alternatives
```bash
# 添加gcc版本（优先级数值越大优先级越高）
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 40 \ 
--slave /usr/bin/g++ g++ /usr/bin/g++-4.8 \
--slave /usr/bin/gcov gcov /usr/bin/gcov-4.8

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 70 \ 
--slave /usr/bin/g++ g++ /usr/bin/g++-7 \
--slave /usr/bin/gcov gcov /usr/bin/gcov-7

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 \ 
--slave /usr/bin/g++ g++ /usr/bin/g++-9 \
--slave /usr/bin/gcov gcov /usr/bin/gcov-9

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 130 \ 
--slave /usr/bin/g++ g++ /usr/bin/g++-13 \
--slave /usr/bin/gcov gcov /usr/bin/gcov-13
```

# 5: 切换默认版本
```bash
# 交互式选择版本
sudo update-alternatives --config gcc

# 输出示例：
There are 3 choices for the alternative gcc (providing /usr/bin/gcc).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/gcc-9     90        auto mode
  1            /usr/bin/gcc-4.8   40        manual mode
  2            /usr/bin/gcc-7     70        manual mode
  3            /usr/bin/gcc-9     90        manual mode

Press <Enter> to keep the current choice[*], or type selection number: 

```

# 6: 版本验证
```bash
gcc --version  # 应显示当前选择的版本
g++ --version  # 应与gcc版本一致
```


