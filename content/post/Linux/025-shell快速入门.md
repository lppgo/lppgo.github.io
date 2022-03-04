---
title: "01-shell快速入门.md"
author: "lucas"
date: 2021-05-30
lastmod: 2021-05-30

tags: ["Linux", "Shell"]
categories: ["Linux"]
keywords: ["Shell", "shell", "脚本"]
---

# Table of Contents

- [Table of Contents](#table-of-contents)
- [1: 第一个 shell 脚本](#1-第一个-shell-脚本)
- [2: 变量 variable](#2-变量-variable)
- [3: 字符串 String](#3-字符串-string)
- [4: 数组 Array](#4-数组-array)
- [5: Shell 参数传递](#5-shell-参数传递)
- [6: 运算](#6-运算)
  - [6.1 算数运算](#61-算数运算)
  - [6.2 关系运算](#62-关系运算)
  - [6.3 布尔运算](#63-布尔运算)
  - [6.4 逻辑运算符](#64-逻辑运算符)
  - [6.5 字符串运算符](#65-字符串运算符)
  - [6.6 文件检测运算符](#66-文件检测运算符)
  - [6.7 布尔运算](#67-布尔运算)
- [7: echo](#7-echo)
- [8: printf](#8-printf)
- [9: test](#9-test)
- [10: 流程控制](#10-流程控制)
  - [10.1 if](#101-if)
  - [10.2 for](#102-for)
  - [10.3 while](#103-while)
  - [10.4 无限循环](#104-无限循环)
  - [10.5 until](#105-until)
  - [10.6 case](#106-case)
  - [10.7 ;;表示 break](#107-表示-break)
- [11: 函数](#11-函数)
  - [11.1 函数定义](#111-函数定义)
  - [11.2 函数参数](#112-函数参数)
  - [11.3 shell 全局变量 和 local 修饰的局部变量](#113-shell-全局变量-和-local-修饰的局部变量)
- [12: 输入输出重定向](#12-输入输出重定向)
- [13: Shell 文件包含](#13-shell-文件包含)
- [14: 常用一些 shell 脚本](#14-常用一些-shell-脚本)
- [15: other](#15-other)

# 1: 第一个 shell 脚本

```bash
#!/bin/bash
echo "hello, world"
```

- 运行程序可以作为解释器参数或者作为可执行程序

```bash
bash test.sh

chmod +x test.sh
test.sh
```

# 2: 变量 variable

```bash
# 1: 变量定义
# 需要注意的是变量名与等号之间不能有空格.
name="huruji"

# 2: 变量使用
# 使用在变量名前添加$即可,{}表示这个变量名的边界.
echo $name
echo ${name}

# 3: 只读变量
# 使用readonly可以将变量定义为只读变量,只读变量不能再次赋值
name="huruji"
readonly name

# 4: 删除变量
# 使用unset删除变量,之后不能再使用.
name="huruji"
unset name
```

# 3: 字符串 String

```bash
# 1: 字符串定义
# 字符串可以使用单引号和双引号,单引号中不能包含单引号,即使转义单引号也不次那个,双引号则可以,双引号也可以使用字符串.
name="huruji"
echo "my name is $name"

# 2: 字符串拼接
name="huruji"
hello="my name is ${name}"
# 3: 获取字符串长度
str="huruji"
echo ${#str} #6
# 4: 提取子字符串
str="huruji"
echo ${str:2:3}
# 5: 字符串查找
str="huruji"
echo `expr index "$str" u`
# 此时输出2,因为此时第一个字符位置从1开始
```

# 4: 数组 Array

```bash
# 1: 数组定义
names=("huruji" "greywind" "xie")
echo ${names[0]}
echo ${names[2]}
# 2: 数组读取
echo ${names[2]}
echo ${names[@]} # 使用@可以获取数组中的所有元素
# 3: 数组长度获取
length1=${#names[@]}
length2=${#names[*]}
echo $length1
echo $length2
```

# 5: Shell 参数传递

- 执行 Shell 脚本的时候,可以向脚本传递参数,在 Shell 中获取这些参数的格式为$n,即$1,$2…….,

```bash
echo "第一个参数是：$1"
echo "第一个参数是：$2"
echo "第一个参数是：$3"

# 运行shell
chmod +x test.sh
test.sh 12 13 14

# 此时输出:
第一个参数是：12
第一个参数是：13
第一个参数是：14
```

- 此外,还有其他几个特殊字符来处理参数
  - $#：传递脚本的参数个数
  - $\*：显示所有的参数
  - $@：返回所有参数
  - $-：显示 Shell 的使用的当前选项
  - $?：退出的状态,0 表示没有错误,其他则表示有错误

# 6: 运算

## 6.1 算数运算

- **算数运算** 原生 bash 不支持简单的数学运算,可以借助于其他命令来完成,例如 awk 和 expr,其中 expr 最常用.expr 是一款表达式计算工具,使用它能完成表达式的求值操作.

```bash
val=`expr 2 + 2`
echo $val
```

- 需要注意的是**运算符两边需要 _空格_ ,且使用的是反引号**. 算术运算符包括：`+ - × / % = == !=`

## 6.2 关系运算

- **关系运算** 关系运算只支持数字,不支持字符串,除非字符串的值是数字.

```bash
a=12
b=13
if [ $a -eq $b ]
	then
	echo "相等"
else
	echo "不等"
fi
```

> 算数运算符：
>
> > -eq：是否相等  
> > -ne：是否不等
> > -gt：大于
> > -lt：小于
> > -ge：大于等于
> > -le：小于等于

## 6.3 布尔运算

> !：非
> -o：或
> -a：与

## 6.4 逻辑运算符

> && : 逻辑与 And
> || ：逻辑或 Or

## 6.5 字符串运算符

## 6.6 文件检测运算符

> 用于检测 Unix 文件的各种属性

下表列出了常用的字符串运算符，假定变量 a 为 "abc"，变量 b 为 "efg"：
|运算符|说明|举例|
|---|---|---|
| = |检测两个字符串是否相等，相等返回 true|[ $a = $b ] 返回 false|
|!= |检测两个字符串是否不相等，不相等返回 true|[ $a != $b ] 返回 true|
| -z|检测字符串长度是否为 0，为 0 返回 true|[ -z $a ] 返回 false|
| -n|检测字符串长度是否不为 0，不为 0 返回 true|[ -n "$a" ] 返回 true|
|str|检测字符串是否为空，不为空返回 true|[ $a ] 返回 true|

## 6.7 布尔运算

```bash
-b：检测文件是否为块设备文件 [ -b $file ]
-c：检测文件是否为字符设备文件 [ -c $file ]
-d：检测文件是否为目录 [ -d $file ]
-f：检测文件是否为普通文件 [ -f $file ]
-g：检测文件是否设置了SGID位 [ -g $file ]
-k：检测文件是否设置了粘着位 [ -k $file ]
-p：检测文件是否是有名管道 [ -p $file ]
-u：检测文件是否设置了SUID位 [ -u $file ]
-r：检测文件是否可读 [ -r $file ]
-w：检测文件是否可写 [ -w $file ]
-x：检测文件是否可执行 [ -x $file ]
-s：检测文件大小是否大于0 [ -s $file ]
-e：检测文件是否存在 [ -e $file ]

    file=”/home/greywind/Desktop/learnShell/test.sh”

    if [ -e $file ] then echo “文件存在” else echo “文件不存在” fi
    if [ -r $file ] then echo “可读” else echo “不可读” fi
    if [ -w $file ] then echo “可写” else echo “不可写” fi
    if [ -x $file ] then echo “可执行” else echo “不可执行” fi
    if [ -d $file ] then echo “是目录” else echo “不是目录” fi
    if [ -f $file ] then echo “是普通文件” else echo “不是普通文件” fi
```

# 7: echo

- echo 在显示输出的时候可以省略双引号,使用`read`命令可以从标准输入中读取一行并赋值给变量

```bash
read name
echo your name is $name
```

- 换行使用转义\n,不换行使用\c 此外使用 > 可以将 echo 结果写入指定文件,这个文件不存在会自动创建

` echo "it is a test" > tmp.log`

- 使用反引号``可以显示命令执行的结果,如 date,history,pwd

```bash
echo `pwd`
echo `date`
```

# 8: printf

- Shell 中的输出命令 printf 类似于 C 语言中的 printf(), 语法格式：

```bash
printf format-string [arguments...]

printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876
```

# 9: test

- test 命令用于检查某个条件是否成立,可以进行数值,字符,文件三方面的测试

```bash
a=100
b=200
if test a == b
	then
	echo "相等"
else
	echo "不等"
fi
```

# 10: 流程控制

## 10.1 if

```bash
a=100
b=200
if test $a -eq $b
	then
	echo "相等"
else
	echo "不等"
fi

a=100
b=200
if test $a -eq $b
	then
	echo "相等"
elif test $a -gt $b
	then
	echo "a大于b"
elif test $a -lt $b
	then
	echo "a小于b"
fi
```

## 10.2 for

```bash
for num in 1 2 3 4
do
	echo ${num}
done

num=10
for((i=1;i<10;i++));
do
	((num=num+10))
done
echo $num
```

## 10.3 while

```bash
num=1
while [ $num -lt 100 ]
do
	((num++))
done

echo $num
```

## 10.4 无限循环

```bash
while:
do
      command
done

while true
do
      command
done

for (( ; ; ))
```

## 10.5 until

```bash
until condition
do
      command
done
```

## 10.6 case

```bash
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

## 10.7 ;;表示 break

- 需要注意的是与其他语言不同 Shell 使用`;;`表示 break,另外没有一个匹配则使用`*`捕获该值
- 与其他语言类似,循环可以使用 break 和 continue 跳出

```bash
echo "输入1 2 3任意一个数字"
read num
case $num in
	1)echo "输入了1"
;;
	2)echo "输入了2"
;;
	3)echo "输入了3"
;;
	*)echo "输入的值不是1 2 3"
;;
esac
```

# 11: 函数

## 11.1 函数定义

- **函数定义** 用户自定义函数可以*使用或者不使用 function 关键字*
- **函数返回值** 同时指定了 return 值则返回这个值,如果没有 return 语句则以最后一条运行结果作为返回值.

```bash
function first(){
	echo "hello world"
}

first(){
	echo "hello world"
}

# 调用函数直接使用这个函数名即可
first
```

## 11.2 函数参数

- 在 Shell 中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1 表示第一个参数，$2 表示第二个参数...

带参数的函数示例：

```bash
#!/bin/bash

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73

# 输出结果：
第一个参数为 1 !
第二个参数为 2 !
第十个参数为 10 !
第十个参数为 34 !
第十一个参数为 73 !
参数总数有 11 个!
作为一个字符串输出所有参数 1 2 3 4 5 6 7 8 9 34 73 !
```

- **注意**，$10 不能获取第十个参数，获取第十个参数需要${10}。`当n>=10时，需要使用${n}来获取参数`。

- 另外，还有几个特殊字符用来处理参数：

| 参数处理 | 说明                                                           |
| -------- | -------------------------------------------------------------- |
| $#       | 传递到脚本或函数的参数个数                                     |
| $\*      | 以一个单字符串显示所有向脚本传递的参数                         |
| $$       | 后台运行的最后一个进程的 ID 号                                 |
| $@       | 与$\*相同，但是使用时加引号，并在引号中返回每个参数。          |
| $-       | 显示 Shell 使用的当前选项，与 set 命令功能相同。               |
| $?       | 显示最后命令的退出状态。0 表示没有错误，其他任何值表明有错误。 |

## 11.3 shell 全局变量 和 local 修饰的局部变量

**`local` 作用**：一般用于 shell 内局部变量的定义，多使用在函数内部

**关于局部变量和全局变量：**
（1）shell 脚本中定义的变量是 global 的，作用域从被定义的地方开始，一直到 shell 结束或者被显示删除的地方为止。
（2）shell 函数定义的变量也是 global 的，其作用域从 函数被调用执行变量的地方 开始，到 shell 或结束或者显示删除为止。函数定义的变量可以是 local 的，其作用域局限于函数内部。但是函数的参数是 local 的。
（3）如果局部变量和全局变量名字相同，那么在这个函数内部，会使用局部变量。

```bash
#!/bin/bash

# 定一个全局变量key
key="hello world"

func() {
    key="这是在函数中调用全局变量key,赋值是作用全局的"
    echo "func():key:{$key}"
}

func_local() {
    local key="这个是在函数中使用local 定义一个key局部变量,赋值作用域是函数内部"
    echo "func_local():key:{$key}"
}

# func
func_local

echo "最后的key:${key}"
```

# 12: 输入输出重定向

- 在上文的例子中可以使用 > 可以将 echo 结果写入指定文件,这就是一种输出重定向,重定向主要有以下：

  - command > file：输出重定向至文件 file
  - command < file：输入重定向至文件 file
  - command » file：输出以追加的方式重定向至文件 file
  - n > file：将文件描述符为 n 的文件重定向至文件 file
  - n » file：将文件描述符为 n 的文件以追加的方式重定向到文件 file
  - n >& m：将输出文件 m 和 n 合并
  - n <& m：将输入文件 m 和 n 合并
  - « tag：将开始标记 tag 和结束标记 tag 之间的内容作为输入

```bash
# 将whoami命令输出保存到user文件中
who >> "./user"
```

# 13: Shell 文件包含

- Shell 脚本可以包含外部脚本,可以很方便的封装一些公用的代码作为一个独立的文件,包含的语法格式如下：

```bash
. filename
# 或
source filename
```

- 如: test1.sh

```bash
echo "hello world"
```

- test.sh

```bash
source ./test1.sh
echo "hello"
```

# 14: 常用一些 shell 脚本

```bash

```

# 15: other

```bash

```
