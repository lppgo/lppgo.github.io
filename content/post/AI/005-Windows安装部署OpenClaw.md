---
title: "01--005-Windows安装部署OpenClaw"
author: "lucas"
date: 2026-03-07
lastmod: 2026-03-07

tags: ["AI","Code","Agent"]
categories: ["AI"]
keywords: ["AI","Tool","OpenClaw","龙虾","Agent"]
---

<div align='center' ><font size='50'>01--Windows安装部署OpenClaw</font></div>


# 1: OpenClaw 介绍
OpenClaw（曾用名 Clawdbot、Moltbot）是一个运行在本地电脑的开源 AI 智能体。

|**Feature**|**Description**|
|---|---|
|操作电脑|以读写文件、操作浏览器、调用系统功能.|
|接入聊天工具|出门在外用手机给它留言，它就能自动干活，还能实时同步截图和执行过程.|
|定时任务系统|用自然语言创建定时任务，如"提醒我7:30打开空调".|
|长期记忆|记忆存储在本地，越用越聪明.|

# 2: OpenClaw 的安装准备


## 2.1: 安装Node.js
 - 访问 Node.js 官网：https://nodejs.org/zh-cn/download
 - 下载 LTS 版本（长期支持版）的 Windows 安装包
 - 双击安装，一路 Next 即可
 - `node -v  查看node版本`
## 2.2: 安装Git
- 访问 Git 官网：https://git-scm.com/install/windows
- 点击下载最新版本
- 双击安装，一路 Next 即可（保持默认选项）
## 2.3: 配置 PowerShell 脚本执行权限
- Windows 默认会拦截安装脚本，需要先放开权限。
  - 步骤 1：以管理员身份打开 PowerShell右键点击「开始」菜单 → 选择「Windows PowerShell (管理员)」
  - 步骤 2：查看当前权限 `Get-ExecutionPolicy -List`,如果 CurrentUser 显示 Restricted，说明不允许运行脚本。
  - 步骤 3：修改权限`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
## 2.4: 准备 API Key

# 3: 安装OpenClaw
## 3.1 安装OpenClaw
- 打开 OpenClaw 官网：https://openclaw.ai/
- 复制 Windows 安装命令
- 打开 PowerShell，粘贴以下命令并回车：`iwr -useb https://openclaw.ai/install.ps1 | iex`
- 或者`iwr -useb https://openclaw.ai/install.ps1 | iex`
- **注意**: 要配置ssh key到github或者``
## 3.2 Run OpenClaw
- 验证是否安装成功,查看oepnclaw的版本`openclaw --version`
- 运行 `openclaw onboard --install-daemon`
- 启动 Gateway`默认 UI 在 http://127.0.0.1:18789/`
- 配置文件默认在 `~/.openclaw/openclaw.json`
- 清除npm缓存：`npm cache clean --force`
- 卸载旧版本：`npm uninstall -g openclaw`
- npm重新安装openclaw：`npm install -g openclaw@latest`
- 如果遇到网络问题，可以尝试使用淘宝镜像：`npm install -g openclaw@latest --registry=https://registry.npmmirror.com`
- 确保Node.js和npm版本是最新的
# 4: 初始化配置OpenClaw
# 5: OpenClaw接入飞书
# 5: OpenClaw接入微信
# 7: OpenClaw 案例
