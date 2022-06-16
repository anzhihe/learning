### RESTful API设计规范

- 域名

应该尽量将API部署在专用域名之下

```
https://api.example.com
```

如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下。

```
https://example.com/api/
```

- 版本

应该将API的版本号放入URL

```
http://www.example.com/app/1.0/apples
 
http://www.example.com/app/1.1/apples
 
http://www.example.com/app/2.0/apples
```

- 路径

对于一个简洁结构，你应该始终用名词。 此外，利用的HTTP方法可以分离网址中的资源名称的操作。

```
GET /products ：将返回所有产品清单
POST /products ：将产品新建到集合
GET /products/4 ：将获取产品4
PATCH /products/4 将更新产品4（部分属性更新）
PUT  /products/4：将更新产品4 （全部属性更新）
```

- HTTP动词

| 请求方法 | 请求地址    | 后端操作                      |
| -------- | ----------- | ----------------------------- |
| GET      | /students   | 获取所有学生                  |
| POST     | /students   | 增加学生                      |
| GET      | /students/1 | 获取编号为1的学生             |
| PUT      | /students/1 | 更新编号为1的学生（全部属性） |
| DELETE   | /students/1 | 删除编号为1的学生             |
| PATCH    | /students/1 | 更新编号为1的学生（部分属性） |

- 过滤信息

```
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
?animal_type_id=1：指定筛选条件
```

- 状态码

```
200 OK - [GET]：服务器成功返回用户请求的数据
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - []：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作
401 Unauthorized - []：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - []：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。
```

- 错误处理

```json
{
	error:"Invalid API key"
}
```

- 返回结果

```
GET /collection：返回资源对象的列表（数组）
GET /collection/resource：返回单个资源对象
POST /collection：返回新生成的资源对象
PUT /collection/resource：返回完整的资源对象
PATCH /collection/resource：返回完整的资源对象
DELETE /collection/resource：返回一个空文档
```

