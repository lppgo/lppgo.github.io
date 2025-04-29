<!--
 * @Author: lucas李平平
 * @Date: 2021-09-01 20:31:01
 * @LastEditTime: 2021-09-07 13:30:13
 * @LastEditors: Please set LastEditors
 * @Description: desc
 * @FilePath: /lppgo.github.io/README.md
-->

# lppgo.github.io

[李平平的个人博客](https://lppgo.github.io/)

golang,rust,python,java

## 学习，记录，分享，成长

1: 主题修改

`git clone https://github.com/olOwOlo/hugo-theme-even themes/even`
```go

https://www.cnblogs.com/wylshkjj/p/18785629

# 标准版
go install github.com/gohugoio/hugo@latest

# 构建扩展版
CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@latest


# 构建扩展/部署版本
CGO_ENABLED=1 go install -tags extended,withdeploy github.com/gohugoio/hugo@latest

````
2: config.toml 配置更新

3: hugo -d docs

4: hugo new posts/xxx.md

5: 书写 md 文档

6: 添加图片

7：删除 docs

8: hugo -d docs

9: hugo

10: hugo --gc --minify --cleanDestinationDir

11: git push

12: 本地预览
`hugo server -D`

13: hugo 版本更新

```go

hugo version

go get -u -v github.com/gohugoio/hugo

```
