
- [1: userdel删除用户](#1-userdel删除用户)
- [2: useradd创建用户](#2-useradd创建用户)
- [3: 新用户使用ssh登录验证](#3-新用户使用ssh登录验证)

# 1: userdel删除用户

```bash
# 若使用userdel haha 命令删除该用户时，并不能删除该用户的所有信息，
# 只是删除了/etc/passwd、/etc/shadow、/etc/group/、/etc/gshadow四个文件里的该账户和组的信息

  [root@localhost /]# userdel haha
  [root@localhost /]# cat /etc/passwd | grep haha
  [root@localhost /]# cat /etc/shadow | grep haha
  [root@localhost /]# cat /etc/group | grep haha
  [root@localhost /]# cat /etc/gshadow | grep haha
  [root@localhost /]# find / -name "*haha*"

# 完全删除用户，慎用！！！
userdel -r haha

```

# 2: useradd创建用户

```bash
# 1 在home手动创建新用户home目录
useradd -d /home/haha haha

# 2 设置密码
passwd haha

# 3 设置sudo权限
（1）su root //进入root用户
（2）vim /etc/sudoers //打开sudo的配置文件
    修改sudoers文件:
    <1> 先找到所示的一行：（root ALL=(ALL)ALL）
    <2> 然后给普通用户haha添加sudo权限，在“root ALL=(ALL)ALL”这一行下面，加入如下图所示的一行(用户名 ALL=(ALL) ALL)，并保存
```

# 3: 新用户使用ssh登录验证

