
- [1: grep 匹配包含 '字符串'的行](#1grep-匹配包含-字符串的行)
- [2: grep 匹配不包含 '字符串'的行，反向匹配](#2-grep-匹配不包含-字符串的行反向匹配)
- [3: grep -E 同时匹配多个关键字–"或"关系](#3grep--e-同时匹配多个关键字或关系)
- [4: 同时匹配多个关键字–"与"关系](#4-同时匹配多个关键字与关系)
- [5: grep 其他操作](#5-grep-其他操作)

Linux: grep 命令，用来匹配文本

# 1: grep 匹配包含 '字符串'的行

```shell
# 匹配文件中包含 scenario 的那一行：
cat manpath.config | grep 'scenario'
```

# 2: grep 匹配不包含 '字符串'的行，反向匹配

```shell
# 匹配文件中不包含 scenario 的那一行：
cat manpath.config| grep -v 'scenario'
```

# 3:grep -E 同时匹配多个关键字–"或"关系

```shell
grep -E "word1|word2|word3" file.txt # 匹配 file.txt 中包含 word1 或 word2 或 word3 的行
egrep '123|abc' filename    # 用egrep同样可以实现
awk '/123|abc/' filename   # awk 的实现方式
```

# 4: 同时匹配多个关键字–"与"关系

```shell
grep word1 file.txt | grep word2 |grep word3 # 必须同时满足三个条件（word1、word2和word3）才匹配。
```

# 5: grep 其他操作

```shell
grep -i pattern files   # 不区分大小写地搜索。默认情况区分大小写，
grep -l pattern files   # 只列出匹配的文件名，
grep -L pattern files   # 列出不匹配的文件名，
grep -w pattern files  # 只匹配整个单词，而不是字符串的一部分（如匹配‘magic’，而不是‘magical’），
grep -C number pattern files # 匹配的上下文分别显示[number]行，
```
