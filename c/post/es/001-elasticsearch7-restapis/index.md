
<div align='center' ><font size='50'>ElasticSearch7-Restful APIs</font></div>

      * [1: /ES-API/说明](#1-es-api说明)
      * [2: Cluster - APIs](#2-cluster---apis)
         * [2.1 查询集群状态](#21-查询集群状态)
         * [2.2 查询集群索引信息](#22-查询集群索引信息)
         * [2.3 使用 help 参数查询](#23-使用-help-参数查询)
         * [2.4 查询集群中的节点信息](#24-查询集群中的节点信息)
      * [3: Index - APIs](#3-index---apis)
         * [3.1 创建索引](#31-创建索引)
         * [3.2 获取索引](#32-获取索引)
         * [3.3 获取全部索引](#33-获取全部索引)
      * [4: Doc - APIs](#4-doc---apis)
         * [4.1 创建文档](#41-创建文档)
         * [4.2 删除文档](#42-删除文档)
         * [4.3 查看文档](#43-查看文档)
         * [4.4 查看该索引下的全部文档](#44-查看该索引下的全部文档)
         * [4.5 覆盖数据](#45-覆盖数据)
         * [4.6 更新数据](#46-更新数据)
      * [5: Mapping - APIs](#5-mapping---apis)
         * [5.1 创建 Mapping](#51-创建-mapping)
         * [5.2 查询 Mapping](#52-查询-mapping)
         * [5.3 查询 template](#53-查询-template)
      * [6: Alias - APIs](#6-alias---apis)
         * [6.1 添加 Alias](#61-添加-alias)
         * [6.2 查询 Alias](#62-查询-alias)
      * [7：查询 - APIs](#7查询---apis)
         * [7.1 条件查询](#71-条件查询)
         * [7.2 匹配查询](#72-匹配查询)
         * [7.3 全量查询](#73-全量查询)
         * [7.4 分页查询](#74-分页查询)
         * [7.5 分页过滤](#75-分页过滤)
         * [7.6 排序查询](#76-排序查询)
         * [7.7 组合查询](#77-组合查询)
         * [7.3 分词查询](#73-分词查询)
         * [7.9 完全匹配查询](#79-完全匹配查询)

## 1: /ES-API/说明

````text
# 基本查询模板

​```json
{
  "query": {
    "bool": {
      "filter": [
        //filter 这后面是过滤条件
        { "term": { "uri": "111111" } }, //客户号
        {
          "range": { "rundata_date": { "gte": "20190108", "lte": "20190110" } }
        } //时间过滤，注意此字段类型，string不能过滤
      ]
    }
  },
  "aggregations": {
    //这里我主要关注一个指标，handleTime字段，标示执行时间，主要对它进行监控
    "avg_handleTime": {
      //可以自己命名
      "avg": {
        "field": "handleTime" //平均执行时间
      }
    },
    "percent_handleTime": {
      "percentiles": {
        "field": "handleTime",
        "percents": [50, 95, 99] //这个是现实 50、95、99的线，从小到大，例如到95%执行时间为1.5s，可以看满足预期的比例
      }
    },
    "min_handleTime": {
      "min": {
        "field": "handleTime" //最小执行时间
      }
    },
    "max_handleTime": {
      "max": {
        "field": "handleTime" //最大执行时间
      }
    }
  },
  "size": 0 //显示几条数据，我这里不需要显示，可以根据需要修改
}

````

````
## /ES-API/Cluster - APIs
​```text
集群相关APIS
````

- **公共 Header 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Query 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Body 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **预执行脚本**

- **后执行脚本**

## 2: Cluster - APIs

### 2.1 查询集群状态

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_cat/health?v

- **请求方式**

> GET

- **Content-Type**

> form-data

- **请求 Query 参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| ------ | ------ | -------- | -------- | -------- |
| v      | -      | Text     | 是       | -        |

- **预执行脚本**

- **后执行脚本**

### 2.2 查询集群索引信息

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_cat/indices?v

- **请求方式**

> GET

- **Content-Type**

> form-data

- **请求 Query 参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| ------ | ------ | -------- | -------- | -------- |
| v      | -      | Text     | 是       | -        |

- **预执行脚本**

- **后执行脚本**

### 2.3 使用 help 参数查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_cat/health?help

- **请求方式**

> GET

- **Content-Type**

> form-data

- **请求 Query 参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| ------ | ------ | -------- | -------- | -------- |
| help   | -      | Text     | 是       | -        |

- **预执行脚本**

- **后执行脚本**

### 2.4 查询集群中的节点信息

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_cat/nodes?v

- **请求方式**

> GET

- **Content-Type**

> form-data

- **请求 Query 参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| ------ | ------ | -------- | -------- | -------- |
| v      | -      | Text     | 是       | -        |

- **预执行脚本**

- **后执行脚本**

## 3: Index - APIs

```text
Index索引，类似于Mysql  中的database
```

- **公共 Header 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Query 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Body 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **预执行脚本**

- **后执行脚本**

### 3.1 创建索引

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study

- **请求方式**

> PUT

- **Content-Type**

> json

- **请求 Body 参数**

- **预执行脚本**

- **后执行脚本**

### 3.2 获取索引

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 3.3 获取全部索引

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_cat/indices?v

- **请求方式**

> GET

- **Content-Type**

> form-data

- **请求 Query 参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| ------ | ------ | -------- | -------- | -------- |
| v      | -      | Text     | 是       | -        |

- **预执行脚本**

- **后执行脚本**

## 4: Doc - APIs

```text
文档相关操作APIs.

该文档对应数据库中 表的行数据 添加的数据格式为 JSON 内容
```

- **公共 Header 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Query 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Body 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **预执行脚本**

- **后执行脚本**

### 4.1 创建文档

```text
{
	"name": "java",
	"age": 27,
	"major": "java"
}

{"name":"张三","age": 20,"mail": "111@qq.com","major":"c","hobby":"羽毛球、乒乓球、足球"}

{"name":"李四","age": 21,"mail": "222@qq.com","major":"c#","hobby":"羽毛球、乒乓球、足球、篮球"}

{"name":"王五","age": 22,"mail": "333@qq.com","major":"++","hobby":"羽毛球、篮球、游泳、听音乐"}

{"name":"赵六","age": 23,"mail": "444@qq.com","major":"Go","hobby":"跑步、游泳"}

{"name":"孙七","age": 24,"mail": "555@qq.com","major":"rust","hobby":"听音乐、看电影"}

```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_doc/017

- **请求方式**

> POST

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
	"name": "阿木",
	"age": 17,
	"level": 2,
	"major": "Go",
	"hobby": "羽毛球、篮球、游泳、听音乐",
	"analyzer": "ik_smart",
	"search_analyzer": "ik_smart"
}
```

- **预执行脚本**

- **后执行脚本**

### 4.2 删除文档

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_doc/001

- **请求方式**

> DELETE

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 4.3 查看文档

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_doc/003

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 4.4 查看该索引下的全部文档

```text
查看该索引下的全部文档
```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 4.5 覆盖数据

```text
这个会覆盖原来的 document id 003 下的数据
```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_doc/003

- **请求方式**

> POST

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
	"name": "lucas学C++",
	"age": 17,
	"major": "Python",
	"level":1
}
```

- **预执行脚本**

- **后执行脚本**

### 4.6 更新数据

```text
其它不变，更新部分字段数据
```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_update/003

- **请求方式**

> POST

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
	"doc": {
		"level": 2
	}
}
```

- **预执行脚本**

- **后执行脚本**

## 5: Mapping - APIs

- **公共 Header 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Query 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Body 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **预执行脚本**

- **后执行脚本**

### 5.1 创建 Mapping

```text
# 1: 创建Mapping需要先创建索引.
# 2: es中对mapping的理解
（1）往es里面直接插入数据，es会自动建立索引，同时建立type以及对应的mapping
（2）mapping中就自动定义了每个field的数据类型
（3）不同的数据类型（比如说text和date），可能有的是exact value，有的是full text
（4）exact value，在建立倒排索引的时候，分词的时候，是将整个值一起作为一个关键词建立到倒排索引中去；full text，会经历各种各样的处理，分词，normaliztion（时态转换，同义词转换，大小写转换），才会建立到倒排索引中去。
（5）exact value和full text类型的field决定了，在一个搜索过来的时候，对exact value field或者是full text field进行搜索的行为不一样，会跟建立倒排索引的行为保持一致；比如说exact value搜索的时候，就是直接按照整个值进行匹配，full text query string，也会进行分词和normalization再去倒排索引中去搜索。
（6）`可以用es的dynamic mapping，让其自动建立mapping，包括自动设置数据类型；也可以提前手动创建index和type的mapping，自己对各个field进行设置，包括数据类型，索引行为，分词器等等`
　　
- mapping就是index的type的元数据，每个type都有一个自己的mapping，决定了数据类型，建立倒排索引的行为，还有进行搜索的行为

　　1、mapping核心的数据类型    string，byte，short，integer，long，float，double，boolean，date
　　2、dynamic mapping
　　true or false --> boolean
　　123 　　　  --> long
　　123.45　　  --> double
　　2017-01-01  --> date
　　"hello world" --> string/text
　　3、查看mapping `GET /index/_mapping/type`
# 3：
![](https://img.cdn.apipost.cn/user/911399/1a3e29abc80f2b23.png)

```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_mapping

- **请求方式**

> PUT

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
  "mapping": {
    "properties": {
      "name": {
        "type": "text", // 可以进行分词查询
        "index": true // 可以索引查询
      }
    //   "age": {
    //     "type": "integer",
    //     // "index": true
    //   },
    //   "major": {
    //     "type": "text",
    //     // "index": true
    //   }
    }
  }
}

```

- **预执行脚本**

- **后执行脚本**

### 5.2 查询 Mapping

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_mapping

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 5.3 查询 template

```text
`在logstash可以定义模版，后续在Logstash更新`
```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_template/study

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

## 6: Alias - APIs

- **公共 Header 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Query 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Body 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **预执行脚本**

- **后执行脚本**

- **说明**

```text
**别名**：通过检索一个索引可以检索多个索引的数据，例如我们每天建一个索引，wsy_20211103,wsy_20211104,wsy_20211105…..

想看到所有有关wsy_*的数据，我们可以通过别名来实现
```

### 6.1 添加 Alias

- **接口状态**

>

- **接口 URL**

>

- **请求方式**

> POST

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 6.2 查询 Alias

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/\_cat/aliases/study

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

## 7：查询 - APIs

- **公共 Header 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Query 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **公共 Body 参数**

| 参数名 | 示例值 | 参数描述 |
| ------ | ------ | -------- |

暂无参数

- **预执行脚本**

- **后执行脚本**

### 7.1 条件查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search?q=name:java

- **请求方式**

> GET

- **Content-Type**

> form-data

- **请求 Query 参数**

| 参数名 | 示例值    | 参数类型 | 是否必填 | 参数描述 |
| ------ | --------- | -------- | -------- | -------- |
| q      | name:java | Text     | 是       | -        |

- **预执行脚本**

- **后执行脚本**

### 7.2 匹配查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
    "query":{
        "match":{
            "name":"java"
        }
    }
}
```

- **预执行脚本**

- **后执行脚本**

### 7.3 全量查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> form-data

- **预执行脚本**

- **后执行脚本**

### 7.4 分页查询

```text
`from` 显示第几页，
`size`为每页显示几条数据
```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
	"query": {
		"match_all": {}
	},
	"from": 0, // 显示第几页
	"size": 10 // 每页页大小
}
```

- **预执行脚本**

- **后执行脚本**

### 7.5 分页过滤

```text
只显示指定字段
```

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
    "query":{
        "match_all":{

        }
    },
    "from":0,
    "size":10,
    "_source":["name","age","major","hobby"], // 过滤
}
```

- **预执行脚本**

- **后执行脚本**

### 7.6 排序查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
    "query":{
        "match_all":{

        }
    },
    "from":0,
    "size":10,
    "_source":["name","age","major","hobby"], // 过滤
    "sort":{
        "age":{
            "order":"desc",
        }
    }
}
```

- **预执行脚本**

- **后执行脚本**

### 7.7 组合查询

- **接口状态**

- **接口 URL**

  > http://localhost:9200/study/\_search

- **请求方式**

  > GET

- **Content-Type**

  > json

- **请求 Body 参数**

```json
{
  "query": {
    "bool": {
      //表示多个条件
      "must": [
        //must 表示多个条件同时成立  should 表示或者的意思
        {
          "match": {
            "major": "Go"
          }
        }
      ],
      "filter": {
        "range": {
          "age": {
            "gt": 18
          }
        }
      }
    }
  }
}
```

### 7.3 分词查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
  "query": {
      "match":{
          "hobby":"音乐", // 分词
      }
  }
}

```

- **预执行脚本**

- **后执行脚本**

### 7.9 完全匹配查询

- **接口状态**

>

- **接口 URL**

> http://localhost:9200/study/\_search

- **请求方式**

> GET

- **Content-Type**

> json

- **请求 Body 参数**

```javascript
{
	"query": {
		"match": {
			"name": "lucas学ES"
		}
	}
}
```

- **预执行脚本**

- **后执行脚本**
