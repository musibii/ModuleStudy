// server.js
// import Koa from 'koa'
// import Router from 'koa-router'
// import bodyParser from 'koa-bodyparser'

const Koa = require('koa')
const Router = require('koa-router')
const bodyParser = require('koa-bodyparser')
const KoaStatic = require('koa-static')
const database = require('./mongodb')
const list = require('./controllers/list');


database();

const app = new Koa()
const router = new Router();
const GraphqlRouter = require('./router')
const port = 4000

app.use(bodyParser());

router.get('/hello', (ctx, next) => {
  ctx.body="hello world"
});

router.post('/addOne', list.addOne)
      .post('/editOne', list.editOne)
      .post('/tickOne', list.tickOne)
      .post('/delOne', list.delOne)
      .get('/getAllList', list.getAllList)

app.use(KoaStatic(__dirname + '/public'));
router.use('', GraphqlRouter.routes())
app.use(router.routes())
   .use(router.allowedMethods());

app.listen(port);

console.log('GraphQL-demo server listen port: ' + port)
