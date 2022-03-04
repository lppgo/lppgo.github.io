
- [1: 使用 Hugo 和 Github Page 搭建 Blogs](#1-使用-hugo-和-github-page-搭建-blogs)
- [2: 更新设置 themes 等操作，保证正常可用](#2-更新设置-themes-等操作保证正常可用)
- [3: Create SSH Deploy Key](#3-create-ssh-deploy-key)
  - [3\.1 生成 key](#31-生成-key)
  - [3\.2 在 GitHub 仓库设置 Deploy Keys 和 Secrets](#32-在-github-仓库设置-deploy-keys-和-secrets)
- [4: 编写 Actions 配置文件](#4-编写-actions-配置文件)
- [5: 编写 deploy\.sh 脚本](#5-编写-deploysh-脚本)
- [6: 在 Github Actions 查看执行情况](#6-在-github-actions-查看执行情况)
- [7: 其他](#7-其他)

# 1: 使用 Hugo 和 Github Page 搭建 Blogs

[如何利用 GitHub Pages 和 Hugo 轻松搭建个人博客？](https://zhuanlan.zhihu.com/p/57361697)

# 2: 更新设置 themes 等操作，保证正常可用

# 3: Create SSH Deploy Key

## 3.1 生成 key

```shell
ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f gh-pages -N ""
# You will get 2 files:
#   gh-pages.pub (public key)
#   gh-pages     (private key)
```

## 3.2 在 GitHub 仓库设置 Deploy Keys 和 Secrets

# 4: 编写 Actions 配置文件

在.github/workflows 里面新建一个 gh_pages.yml

```yaml
name: GitHub Page Deploy

on:
  push:
    branches:
      - main
jobs:
  build-deploy:
    runs-on: ubuntu-20.04
    steps:
      - name: Checkout main
        uses: actions/checkout@v1
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: "0.68.0"
          extended: true

      - name: Build Hugo
        run: |
          hugo

      - name: Deploy Hugo to gh-pages
        uses: peaceiris/actions-gh-pages@v2
        env:
          ACTIONS_DEPLOY_KEY: ${{ secrets.ACTIONS_DEPLOY_KEY }}
          PUBLISH_BRANCH: main
          PUBLISH_DIR: ./public
```

# 5: 编写 deploy.sh 脚本

deploy.sh

```shell
#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.
rm -rf docs

hugo -d docs

hugo -t meme

# Add changes to git.
git add -A

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push origin main

```

# 6: 在 Github Actions 查看执行情况

![查看Github Actions 执行情况](/images/微信截图_20210414171619.png)

注意：首次脚本可能会提示如下,点击授权即可

```go
Please visit https://github.com/lppgo/lppgo.github.io/settings/keys/52070463
to approve this key so we know it's safe.
```

# 7: 其他

由于不想维护多个分支，故只做提交，就可以自动生效。

```shell
#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# Build the project.

echo -e "\033[0;32mrm-rf docs\033[0m"
rm -rf docs

echo -e "\033[0;32mhugo -d docs\033[0m"
hugo -d docs

echo -e "\033[0;32mhugo --gc --minify --cleanDestinationDir\033[0m"
hugo --gc --minify --cleanDestinationDir


# Add changes to git.
echo -e "\033[0;32mgit status\033[0m"
git status
echo -e "\033[0;32mgit add -A\033[0m"
git add -A

# # Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
echo -e "\033[0;32mgit commit -m "$msg"\033[0m"
git commit -m "$msg"


# Push source and build repos.
echo -e "\033[0;32mgit push origin main\033[0m"
git push origin main

```
