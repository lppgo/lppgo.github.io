
- [1: 直接在配置文件中修改](#1-直接在配置文件中修改)
- [2: 使用系统管理工具 update-alternatives](#2-使用系统管理工具-update-alternatives)
- [3: 完全删除 nano](#3-完全删除-nano)
- [4：vim 操作命令](#4vim-操作命令)
  - [4.1 日志定位](#41-日志定位)
  - [4.2 按行截取](#42-按行截取)
  - [4.3 数据统计](#43-数据统计)
  - [4.4 其他常用命令 summary](#44-其他常用命令-summary)

# 1: 直接在配置文件中修改

```shell
echo export EDITOR=/usr/bin/vim >> ~/.bashrc
```

# 2: 使用系统管理工具 update-alternatives

`sudo update-alternatives --config editor`
`update-alternatives --config editor`

```shell
xxx:~$ update-alternatives --config editor
有 4 个候选项可用于替换 editor (提供 /usr/bin/editor)。

 选择       路径              优先级  状态
------------------------------------------------------------
* 0            /bin/nano            40        自动模式
 1            /bin/ed             -100       手动模式
 2            /bin/nano            40        手动模式
 3            /usr/bin/vim.basic   30        手动模式
 4            /usr/bin/vim.tiny    10        手动模式

要维持当前值[*]请按<回车键>，或者键入选择的编号：3
```

# 3: 完全删除 nano

如果系统中只剩下 nano 和 vim 两个编辑器，完全删除 nano，那么系统会默认选择 vim 为默认编辑器 在终端输入删除 nano 编辑器的命令：

```shell
apt-get remove nano
```

# 4：vim 操作命令

## 4.1 日志定位

```bash
    vim aa-system.log #打开编辑器
    :set number #设置显示行号

    G #跳至最后一行
    ?querykeywords #向上搜索关键词
    n #向上重复搜索
    N #向下重复搜索

    gg #跳至第一行
    /querykeywords #向下搜索关键词
    n #向下重复搜索
    N #向上重复搜索

    ctrl + b  #向上移动一页
    ctrl + d  #向下移动半页
```

## 4.2 按行截取

```bash
    set number #显示行
    : 16, 27 w subfile.log      #截取16到27行到另外一个文件subfile.log中
    : 16, 27 w >> subefile.log  #截取16到27行，并追加到另外一个文档subfile.log中
```

## 4.3 数据统计

```bash
    :%s/objStr//gn  #统计objStr字符串在文档中的次数
```

## 4.4 其他常用命令 summary

```bash
    :set nonumber #关闭显示行号
    gg #跳至首行
    G #调至行尾

    ? #向前搜索
    / #向后搜索

    ctrl + e #上滚
    ctrl + y #下滚

    yy #拷贝
    Y #拷贝行
    P #粘贴(前)
    p #粘贴(后)

    ctrl + f #向下移动一页
    ctrl + u #向上移动半页
    ctrl + b  #向上移动一页
    ctrl + d  #向下移动半页

    less命令

```
