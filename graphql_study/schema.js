// //schema.js
// const {
//       GraphQLSchema,
//       GraphQLObjectType,
//       GraphQLString,
//     } = require('graphql');
// const queryObj = new GraphQLObjectType({
//     name: 'myFirstQuery',
//     description: 'a hello world demo',
//     fields: {
//         hello: {
//             name: 'a hello world query',
//             description: 'a hello world demo',
//             type: GraphQLString,
//             resolve(parentValue, args, request) {
//                 return 'hello world !';
//             }
//         }
//     }
// });
// module.exports = new GraphQLSchema({
//   query: queryObj
// });

// 启动项目需要安装的包
// 新建一个graphql文件夹，然后在该目录下打开终端，执行npm init --y初始化一个packjson文件。
// 安装依赖包：npm install --save -D express express-graphql graphql
// 新建schema.js文件，填上下面的代码
const {
      GraphQLSchema,
      GraphQLObjectType,
      GraphQLString,
      GraphQLInt,
      GraphQLBoolean
    } = require('graphql');

const queryObj = new GraphQLObjectType({
    name: 'myFirstQuery',
    description: 'a hello world demo',
    fields: {
        hello: {
            name: 'a hello world query',
            description: 'a hello world demo',
            type: GraphQLString,
            args: {
                name: {  // 这里定义参数，包括参数类型和默认值
                    type: GraphQLString,
                    defaultValue: 'Brian'
                }
            },
            resolve(parentValue, args, request) { // 这里演示如何获取参数，以及处理
                return 'hello world ' + args.name + '!';
            }
        },
        person: {
            name: 'personQuery',
            description: 'query a person',
            type: new GraphQLObjectType({ // 这里定义查询结果包含name,age,sex三个字段，并且都是不同的类型。
                name: 'person',
                fields: {
                  name: {
                    type: GraphQLString
                  },
                  age: {
                    type: GraphQLInt
                  },
                  sex: {
                    type: GraphQLBoolean
                  }
                }
            }),
            args: {
                name: {
                    type: GraphQLString,
                    defaultValue: 'Charming'
                }
            },
            resolve(parentValue, args, request) {
                return {
                    name: args.name,
                    age: args.name.length,
                    sex: Math.random() > 0.5
                };
            }
        }
    }
});

module.exports = new GraphQLSchema({
  query: queryObj
});

