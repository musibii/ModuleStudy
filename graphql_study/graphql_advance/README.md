# 搭配 koa 实现一个 graphql 查询的例子
逐步从简单的 koa 服务到 MongoDB 的数据插入查询，再到 graphql 的使用，最终实现用 graphql 对数据库的增删查改

1. 初始化项目
- 初始化项目，在根目录下运行`npm init --y`
- 安装依赖包：`npm install koa koa-static koa-router koa-bodyparser mongoose --save -D`
- 新建`config`、`controllers`、`graphql`、`mongodb`、`public`、`router` 这几个文件夹
2. 跑一个 koa 服务器
