// import { graphqlKoa, graphiqlKoa } from 'graphql-server-koa'
// import {addOne, getAllList, editOne, tickOne, delOne} from '../controllers/list'
const graphql_server_koa = require('graphql-server-koa')
const list = require('../controllers/list');

// import schema from '../graphql/schema'
const schema = require('../graphql/schema')

const router = require('koa-router')()

router.post('/addOne', list.addOne)
      .post('/editOne', list.editOne)
      .post('/tickOne', list.tickOne)
      .post('/delOne', list.delOne)
      .get('/getAllList', list.getAllList)

router.post('/graphql', async (ctx, next) => {
        await graphql_server_koa.graphiqlKoa({schema: schema})(ctx, next)
      })
      .get('/graphql', async (ctx, next) => {
        await graphql_server_koa.graphiqlKoa({schema: schema})(ctx, next)
      })
      .get('/graphiql', async (ctx, next) => {
        await graphql_server_koa.graphiqlKoa({endpointURL: '/graphql'})(ctx, next)
      })

module.exports = router