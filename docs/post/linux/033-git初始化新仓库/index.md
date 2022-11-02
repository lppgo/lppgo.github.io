
# 1: 使用 docker 安装配置 gitlab

- 设置默认分支。默认是`main`,更改为`master`
-

# 2: 初始化新仓库

- 在 gitlab 创建新仓库
- 把本地目录上传到这个仓库

```go
cd xxx
git init
git add -A
git commit -m "init"
git remote add origin http://47.115.218.14:9980/ms/oems-test-v3.git
git branch -M master
git push -uf origin master
```

- `You are not allowed to force push code to a protected branch on this project.`主要原因是因为向一个受保护的分支强制提交了代码，可以在仓库里面进行设置来解决这个问题.
