
- [1: Git Config](#1-git-config)
  - [1.1 Git global setup 全局设置](#11-git-global-setup-全局设置)
  - [1.2 修改 git config](#12-修改-git-config)
- [2: 仓库 Repository 管理](#2-仓库repository管理)
  - [2.1 clone 仓库](#21-clone仓库)
  - [2.2 Create a new repository 创建一个新仓库](#22-create-a-new-repository-创建一个新仓库)
  - [2.3 Push an existing folder 推送一个已存在的文件夹](#23-push-an-existing-folder-推送一个已存在的文件夹)
  - [2.5 Push an existing Git repository 推送一个已存在的仓库](#25-push-an-existing-git-repository-推送一个已存在的仓库)
- [3: History 管理](#3-history管理)
  - [3.1 查看历史](#31-查看历史)
  - [3.2 Tag 标签](#32-tag标签)
  - [3.3 Rollback 回滚](#33-rollback回滚)
  - [3.4 取消文件的修改](#34-取消文件的修改)
  - [3.5 删除文件](#35-删除文件)
  - [3.6 移动文件](#36-移动文件)
  - [3.7 查看文件的修改](#37-查看文件的修改)
  - [3.8 暂存和恢复当前 staging](#38-暂存和恢复当前staging)
  - [3.9 修改 commit 历史记录](#39-修改commit历史记录)
- [4: Branch 分支管理](#4-branch分支管理)
  - [4.1 创建分支](#41-创建分支)
  - [4.2 查看分支](#42-查看分支)
  - [4.3 合并分支](#43-合并分支)
  - [4.4 Stash 当前分支中未提交的修改移动到其他分支](#44-stash-当前分支中未提交的修改移动到其他分支)
  - [4.5 强制更新到远程分支最新版本](#45-强制更新到远程分支最新版本)
- [5: Submodule 使用](#5-submodule使用)
  - [5.1 克隆带 submodule 的库](#51-克隆带submodule的库)
  - [5.2 clone 主库后再去 clone submodule](#52-clone主库后再去clone-submodule)
- [6: 更新与发布](#6-更新与发布)
  - [6.1 列出当前配置的远程端](#61-列出当前配置的远程端)
  - [6.2 显示远程端的信息](#62-显示远程端的信息)
  - [6.3 添加新的远程端](#63-添加新的远程端)
  - [6.4 下载远程端版本,但不合并到 HEAD 中](#64-下载远程端版本但不合并到head中)
  - [6.5 下载远程端版本,并自动与 HEAD 版本合并](#65-下载远程端版本并自动与head版本合并)
  - [6.6 将远程端版本合并到本地版本中](#66-将远程端版本合并到本地版本中)
  - [6.7 以 rebase 方式将远端分支与本地合并](#67-以rebase方式将远端分支与本地合并)
  - [6.8 将本地版本发布到远程端](#68-将本地版本发布到远程端)
  - [6.9 删除远程端分支](#69-删除远程端分支)
  - [6.10 发布标签](#610-发布标签)
  - [6.11 以 rebase 方式将远端分支与本地合并](#611-以rebase方式将远端分支与本地合并)
- [7: 合并(Merge)与重置(Rebase)](#7-合并merge与重置rebase)
  - [7.1 将分支合并](#71-将分支合并)
  - [7.2 退出 rebase](#72-退出rebase)
  - [7.3 合并提交](#73-合并提交)
- [8: 撤销 revoke](#8-撤销revoke)
  - [8.1 放弃工作目录下的所有修改](#81-放弃工作目录下的所有修改)
  - [8.2 移除缓存区的所有文件（i.e. 撤销上次 git add）](#82-移除缓存区的所有文件ie-撤销上次git-add)
  - [8.3 放弃某个文件的所有本地修改](#83-放弃某个文件的所有本地修改)
  - [8.4 重置一个提交（通过创建一个截然不同的新提交）](#84-重置一个提交通过创建一个截然不同的新提交)
  - [8.5 将 HEAD 重置到指定的版本,并抛弃该版本之后的所有修改](#85-将head重置到指定的版本并抛弃该版本之后的所有修改)
  - [8.6 用远端分支强制覆盖本地分支](#86-用远端分支强制覆盖本地分支)
  - [8.7 将 HEAD 重置到上一次提交的版本,并将之后的修改标记为未添加到缓存区的修改](#87-将head重置到上一次提交的版本并将之后的修改标记为未添加到缓存区的修改)
  - [8.8 将 HEAD 重置到上一次提交的版本,并保留未提交的本地修改](#88-将head重置到上一次提交的版本并保留未提交的本地修改)
  - [8.9 删除添加.gitignore 文件前错误提交的文件](#89-删除添加gitignore文件前错误提交的文件)

![](https://i0.hdslb.com/bfs/album/c61199aeb14daf36e493529c32d0fe8a56b03e28.jpg)

# 1: Git Config

- Git 的全局设置在~/.gitconfig 中,单独设置-在 project/.git/config 下.

- 忽略设置全局在~/.gitignore_global 中,单独设置在 project/.gitignore 下.

## 1.1 Git global setup 全局设置

```bash
# git config --global --list

url.“https://”.insteadof=git://
http.postbuffer=1048576000
lucas.email=golpp@qq.com
user.name=lpp
user.password=xxx
user.email=1605577372@qq.com
credential.helper=store
core.quotepath=false
gui.encoding=utf-8
i18n.commitencoding=utf-8
i18n.logoutputencoding=utf-8
sendpack.sideband=false
init.defaultbranch=main

```

## 1.2 修改 git config

```bash
# 设置 commit 的用户和邮箱
git config --global user.name  "xxxx"

git config --global user.email  "xxxx"

# 或者直接修改config文件
[user]
    name = xxx
    email = xxx@xxx.com
```

```bash
# 设置git终端颜色
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
```

# 2: 仓库 Repository 管理

## 2.1 clone 仓库

```bash
git clone https://github.com/golang/golang-src.git
git clone --depth=1 https://github.com/golang/golang-src.git # 只抓取最近的一次 commit
```

## 2.2 Create a new repository 创建一个新仓库

```bash
git clone http://192.168.1.100/myproject/test.git
cd test
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

## 2.3 Push an existing folder 推送一个已存在的文件夹

```bash
cd existing_folder
git init
git remote add origin http://192.168.1.100/myproject/test.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

## 2.5 Push an existing Git repository 推送一个已存在的仓库

```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin http://192.168.1.100/myproject/test.git
git push -u origin --all
git push -u origin --tags
```

# 3: History 管理

## 3.1 查看历史

```bash
git log --pretty=oneline filename # 一行显示
git show xxxx # 查看某次修改
```

## 3.2 Tag 标签

```bash
git tag # 显示所有标签
git tag -l 'v1.4.2.*' # 显示 1.4.2 开头标签
git tag v1.3 # 简单打标签
git tag -a v1.2 9fceb02 # 后期加注标签
git tag -a v1.4 -m 'my version 1.4' # 增加标签并注释, -a 为 annotated 缩写
git show v1.4 # 看某一标签详情
git push origin v1.5 # 分享某个标签
git push origin --tags # 分享所有标签
```

## 3.3 Rollback 回滚

```bash
git reset 9fceb02 # 保留修改
git reset 9fceb02 --hard # 删除之后的修改
```

## 3.4 取消文件的修改

```bash
git checkout -- a.golang #  取消单个文件
git checkout -- # 取消所有文件的修改
```

## 3.5 删除文件

```bash
git rm a.golang  # 直接删除文件
git rm --cached a.golang # 删除文件暂存状态
```

## 3.6 移动文件

```bash
git mv a.golang ./test/a.golang
```

## 3.7 查看文件的修改

```bash
git diff          # 查看未暂存的文件更新
git diff --cached # 查看已暂存文件的更新
```

## 3.8 暂存和恢复当前 staging

```bash
git stash # 暂存当前分支的修改
git stash apply # 恢复最近一次暂存
git stash list # 查看暂存内容
git stash apply stash@{2} # 指定恢复某次暂存内容
git stash drop stash@{0} # 删除某次暂存内容
git stash pop #  从git栈中获取到最近一次stash进去的内容，恢复工作区的内容。获取之后，会删除栈中对应的stash
 git stash clear # 清空git栈
```

## 3.9 修改 commit 历史记录

```bash
git rebase -i 0580eab8
```

# 4: Branch 分支管理

## 4.1 创建分支

```bash
git branch develop # 只创建分支
git checkout -b master develop # 创建并切换到 develop 分支
```

## 4.2 查看分支

```bash
git branch # 查看本地分支
git branch -r # 查看remote分支
git branch -a # 查看所有分支
```

## 4.3 合并分支

```bash
git checkout master # 切换到 master 分支
git merge --no-ff develop # 把 develop 合并到 master 分支,no-ff 选项的作用是保留原分支记录
git rebase develop # rebase 当前分支到 develop
git branch -d develop # 删除 develop 分支
```

## 4.4 Stash 当前分支中未提交的修改移动到其他分支

```bash
git stash
git checkout branch2
git stash pop
```

## 4.5 强制更新到远程分支最新版本

```bash
git reset --hard origin/master
git submodule update --remote -f
```

# 5: Submodule 使用

## 5.1 克隆带 submodule 的库

```bash
git clone --recursive https://github.com/chaconinc/MainProject
```

## 5.2 clone 主库后再去 clone submodule

```bash
git clone https://github.com/chaconinc/MainProject
git submodule init
git submodule update
```

# 6: 更新与发布

## 6.1 列出当前配置的远程端

```bash
git remote -v
```

## 6.2 显示远程端的信息

```bash
git remote show <remote>
```

## 6.3 添加新的远程端

```bash
git remote add <remote> <url>
```

## 6.4 下载远程端版本,但不合并到 HEAD 中

```bash
 git fetch <remote>
```

## 6.5 下载远程端版本,并自动与 HEAD 版本合并

```bash
 git remote pull <remote> <url>
```

## 6.6 将远程端版本合并到本地版本中

```bash
将远程端版本合并到本地版本中

```

## 6.7 以 rebase 方式将远端分支与本地合并

```bash
git pull --rebase <remote> <branch>
```

## 6.8 将本地版本发布到远程端

```bash
git push remote <remote> <branch>
```

## 6.9 删除远程端分支

```bash
git push <remote> :<branch> (since Git v1.5.0)
or
git push <remote> --delete <branch> (since Git v1.7.0)
```

## 6.10 发布标签

```bash
git push --tags
```

## 6.11 以 rebase 方式将远端分支与本地合并

# 7: 合并(Merge)与重置(Rebase)

## 7.1 将分支合并

```bash
# merge
git merge <branch>

# rebase
git rebase <branch>
```

## 7.2 退出 rebase

`git rebase --abort`

## 7.3 合并提交

```bash
git rebase -i <commit-just-before-first>
```

把上面的内容替换为下面的内容：

```bash
pick <commit_id>
pick <commit_id2>
pick <commit_id3>
```

替换为:

```bash
pick <commit_id>
squash <commit_id2>
squash <commit_id3>
```

# 8: 撤销 revoke

## 8.1 放弃工作目录下的所有修改

`git reset --hard HEAD`

## 8.2 移除缓存区的所有文件（i.e. 撤销上次 git add）

`git reset HEAD`

## 8.3 放弃某个文件的所有本地修改

`git checkout HEAD <file>`

## 8.4 重置一个提交（通过创建一个截然不同的新提交）

`git revert <commit>`

## 8.5 将 HEAD 重置到指定的版本,并抛弃该版本之后的所有修改

`git reset --hard <commit>`

## 8.6 用远端分支强制覆盖本地分支

```bash
git reset --hard <remote/branch> e.g., upstream/master, origin/my-feature
```

## 8.7 将 HEAD 重置到上一次提交的版本,并将之后的修改标记为未添加到缓存区的修改

```bash
git reset <commit>
```

## 8.8 将 HEAD 重置到上一次提交的版本,并保留未提交的本地修改

```bash
 git reset --keep <commit>
```

## 8.9 删除添加.gitignore 文件前错误提交的文件

```bash
$ git rm -r --cached .
$ git add .
$ git commit -m "remove xyz file"
```
