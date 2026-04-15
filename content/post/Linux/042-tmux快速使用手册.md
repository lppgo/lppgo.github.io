---
title: "01-tmux快速使用手册"
author: "lucas"
date: 2026-04-15
lastmod: 2026-04-15

tags: ["Linux", "tmux"]
categories: ["Linux"]
keywords: ["linux", "tmux"]
---

# tmux 使用速查（面向 Claude TUI 场景）

## 1. 先记住 tmux 的 3 个层级

- `session`：一个独立会话，像一整套工作台
- `window`：会话里的标签页
- `pane`：窗口里的分屏

你现在最需要会的是：

- 新建
- 进入
- 退出
- 查看
- 给 Claude 发输入
- 抓输出

---

## 2. 最常用的 6 个命令

### 2.1 新建一个 tmux 会话

```bash
tmux new-session -d -s claude-work
```

含义：

- `new-session`：新建会话
- `-d`：先放后台，不立刻进去
- `-s claude-work`：会话名字叫 `claude-work`

---

### 2.2 查看当前有哪些会话

```bash
tmux list-sessions
```

也可以简写为：

```bash
tmux ls
```

---

### 2.3 进入某个会话

```bash
tmux attach -t claude-work
```

含义：

- `attach`：连接进去
- `-t claude-work`：目标会话名

---

### 2.4 临时退出 tmux，但不关掉里面的程序

按键：

```text
Ctrl+b
然后按 d
```

这叫 `detach`。

---

### 2.5 强制接管一个会话

```bash
tmux attach -d -t claude-work
```

含义：

- `-d`：如果别人已经连着这个 session，先踢掉对方，再让你接管

---

### 2.6 杀掉一个会话

```bash
tmux kill-session -t claude-work
```

含义：

- 直接关闭这个 session，里面的程序也会结束

---

## 3. tmux 最重要的按键前缀

tmux 里所有快捷键，都先按：

```text
Ctrl+b
```

然后再按后续键。

常见组合：

- `Ctrl+b d`：detach，临时退出当前 tmux
- `Ctrl+b c`：新建 window
- `Ctrl+b ,`：重命名当前 window
- `Ctrl+b %`：左右分屏
- `Ctrl+b "`：上下分屏
- `Ctrl+b o`：切换到下一个 pane

---

## 4. window 怎么用

### 4.1 新建 window

在 tmux 里按：

```text
Ctrl+b c
```

这会创建一个新标签页。

---

### 4.2 查看所有 window

```bash
tmux list-windows -t claude-work
```

---

### 4.3 切换到某个 window

```bash
tmux select-window -t claude-work:1
```

含义：

- `claude-work:1` = session 名 + window 编号 `1`

---

## 5. pane 怎么用

### 5.1 左右分屏

```text
Ctrl+b %
```

### 5.2 上下分屏

```text
Ctrl+b "
```

### 5.3 在分屏间切换

```text
Ctrl+b o
```

### 5.4 关闭当前 pane

在 pane 里输入：

```bash
exit
```

或者按：

```text
Ctrl+d
```

---

## 6. 给 Claude TUI 发命令

这是最关键的部分。

假设你已经有一个 tmux 会话叫 `claude-work`，你可以这样启动 Claude：

```bash
tmux new-session -d -s claude-work
tmux send-keys -t claude-work 'cd /root/proj/go/lms_monitor && claude' Enter
```

含义：

- 先开 session
- 再往里面发送一条命令
- `Enter` 相当于回车

然后你可以继续发提示词：

```bash
tmux send-keys -t claude-work '帮我分析这个项目的登录流程' Enter
```

如果 Claude 在等你输入，你再发下一条：

```bash
tmux send-keys -t claude-work '继续，把数据库相关逻辑也检查一下' Enter
```

---

## 7. 看 Claude 当前跑到哪了

抓屏输出：

```bash
tmux capture-pane -t claude-work -p -S -80
```

参数解释：

- `capture-pane`：抓当前屏幕
- `-p`：直接打印出来
- `-S -80`：从倒数 80 行开始抓

如果你想看更多：

```bash
tmux capture-pane -t claude-work -p -S -200
```

---

## 8. 一个完整的 Claude + tmux 工作流

你可以直接照着敲：

### 8.1 创建会话

```bash
tmux new-session -d -s claude-work
```

### 8.2 启动 Claude

```bash
tmux send-keys -t claude-work 'cd /root/proj/go/lms_monitor && claude' Enter
```

### 8.3 等它启动后，发第一条任务

```bash
tmux send-keys -t claude-work '先帮我梳理这个项目的目录结构' Enter
```

### 8.4 过几秒抓屏看进度

```bash
tmux capture-pane -t claude-work -p -S -80
```

### 8.5 如果它问你问题，就继续发补充指令

```bash
tmux send-keys -t claude-work '是的，继续往下分析' Enter
```

### 8.6 不想盯着看了就 detach

```text
Ctrl+b d
```

### 8.7 之后再回来

```bash
tmux attach -t claude-work
```

---

## 9. 最值得先记住的命令清单

```bash
tmux new-session -d -s claude-work
tmux ls
tmux attach -t claude-work
tmux attach -d -t claude-work
tmux kill-session -t claude-work
tmux send-keys -t claude-work '命令内容' Enter
tmux capture-pane -t claude-work -p -S -80
tmux list-windows -t claude-work
tmux select-window -t claude-work:1
```

---

## 10. 建议你的第一轮练习

先执行：

```bash
tmux new-session -d -s test
tmux attach -t test
```

进入后按：

```text
Ctrl+b c
```

创建一个 window。

再按：

```text
Ctrl+b %
```

左右分屏。

然后按：

```text
Ctrl+b d
```

退出但不关闭。

最后执行：

```bash
tmux ls
```

你会看到这个 session 还在。
