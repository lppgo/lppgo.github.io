---
title: "037-Linux配置环境变量的6种方法"
author: "lucas"
date: 2022-12-23
lastmod: 2022-12-23

tags: ["Linux", "运维"]
categories: ["Linux"]
keywords: ["Linux", "环境变量"]
---

<!-- [toc] -->

<div align="center"><font size="35">Linux配置环境变量的6种方法</font></div>

- [1: Linux 读取环境变量](#1-linux-读取环境变量)
  - [1.1 export PATH](#11-export-path)
  - [1.2 vim ~/.bashrc](#12-vim-bashrc)
  - [1.3 vim ~/.bash_profile](#13-vim-bash_profile)
  - [1.4 vim /etc/bashrc](#14-vim-etcbashrc)
  - [1.5 vim /etc/profile](#15-vim-etcprofile)
  - [1.6 vim /etc/environment](#16-vim-etcenvironment)
- [2: Linux 环境变量加载原理解析](#2-linux-环境变量加载原理解析)
  - [2.1 环境变量的分类](#21-环境变量的分类)
  - [2.2 Linux 环境变量文件加载详解](#22-linux-环境变量文件加载详解)

---

# 1: Linux 读取环境变量

- 在自定义安装软件的时候，经常需要配置环境变量，下面列举出各种对环境变量的配置方法。

- 下面所有例子的环境说明如下：

  - 系统：Ubuntu 14.0
  - 用户名：uusama
  - 需要配置 MySQL 环境变量路径：/home/uusama/mysql/binct)

- **读取环境变量的方法：**
  - **export** 命令显示当前系统定义的所有环境变量
  - **echo $PATH** 命令输出当前的 PATH 环境变量的值

## 1.1 export PATH

- 使用 export 命令直接修改 PATH 的值，配置 MySQL 进入环境变量的方法:`export PATH=/home/uusama/mysql/bin:PATH`
- **注意事项：**
  - 生效时间：立即生效
  - 生效期限：当前终端有效，窗口关闭后无效
  - **生效范围**：仅对当前用户有效
  - 配置的环境变量中不要忘了加上原来的配置，即$PATH 部分，避免覆盖原来配置

## 1.2 vim ~/.bashrc

- 通过修改用户目录下的~/.bashrc 文件进行配置：

```bash
vim ~/.bashrc

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

- **注意事项：**
  - 生效时间：使用相同的用户打开新的终端时生效，或者手动 `source ~/.bashrc` 生效
  - 生效期限：永久有效
  - 生效范围：仅对当前用户有效
  - 如果有后续的环境变量加载文件覆盖了 PATH 定义，则可能不生效

## 1.3 vim ~/.bash_profile

- 修改~/.bashrc 文件类似，也是要在文件最后加上新的路径即可：

```bash
vim ~/.bash_profile

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

- **注意事项：**
  - 生效时间：使用相同的用户打开新的终端时生效，或者手动`source ~/.bash_profile`生效
  - 生效期限：永久有效
  - 生效范围：仅对当前用户有效
  - 如果没有~/.bash_profile 文件，则可以编辑~/.profile 文件或者新建一个

## 1.4 vim /etc/bashrc

- **该方法是修改系统配置，需要管理员权限（如 root）或者对该文件的写入权限：**

```bash
# 如果/etc/bashrc文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/bashrc

vim /etc/bashrc

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

- **注意事项：**

  - 生效时间：新开终端生效，或者手动`source /etc/bashrc`生效
  - 生效期限：永久有效
  - **生效范围**：对所有用户有效,global 全局有效

## 1.5 vim /etc/profile

- **该方法修改系统配置，需要管理员权限或者对该文件的写入权限，和 vim /etc/bashrc 类似：**

```bash
# 如果/etc/profile文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/profile

vim /etc/profile

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

- **注意事项：**

  - 生效时间：新开终端生效，或者手动`source /etc/profile`生效
  - 生效期限：永久有效
  - **生效范围**：对所有用户有效,global 全局有效

## 1.6 vim /etc/environment

- **该方法是修改系统环境配置文件，需要管理员权限或者对该文件的写入权限：**

```bash
# 如果/etc/bashrc文件不可编辑，需要修改为可编辑
chmod -v u+w /etc/environment

vim /etc/profile

# 在最后一行加上
export PATH=$PATH:/home/uusama/mysql/bin
```

- **注意事项：**

  - 生效时间：新开终端生效，或者手动`source /etc/environment`生效
  - 生效期限：永久有效
  - **生效范围**：对所有用户有效,global 全局有效

# 2: Linux 环境变量加载原理解析

- 上面列出了环境变量的各种配置方法，那么 Linux 是如何加载这些配置的呢？是以什么样的顺序加载的呢？
- 特定的加载顺序会导致相同名称的环境变量定义被覆盖或者不生效。

## 2.1 环境变量的分类

> 环境变量可以简单的分成用户自定义的环境变量以及系统级别的环境变量。

- **用户级别环境变量定义文件**：~/.bashrc、~/.profile（部分系统为：~/.bash_profile）
- **系统级别环境变量定义文件**：/etc/bashrc、/etc/profile(部分系统为：/etc/bash_profile）、/etc/environment
  另外在用户环境变量中，系统会首先读取~/.bash_profile（或者~/.profile）文件，如果没有该文件则读取~/.bash_login，根据这些文件中内容再去读取~/.bashrc。

## 2.2 Linux 环境变量文件加载详解

由上面的测试可容易得出 Linux 加载环境变量的顺序如下，：

- 系统环境变量 -> 用户自定义环境变量 /etc/environment -> /etc/profile -> ~/.profile
- 打开/etc/profile 文件你会发现，该文件的代码中会加载/etc/bash.bashrc 文件，然后检查/etc/profile.d/目录下的.sh 文件并加载。
- /.profile 文件只在用户登录的时候读取一次，而/.bashrc 会在每次运行 Shell 脚本的时候读取一次。
