## 1. 软件架构
- 什么是软件

软件是与计算机系统操作有关的程序、规程、规则及任何与之有关的文档及数据的完整集合

- 什么是框架

大家身体都有五脏六腑，每个器官都在旅行自己的职责，各个器官配合来完成生命的活动。那我们就可以把身体想象成一个框架。软件框架是由其中的各个模块组成的，每个模块负责自己的功能，模块与模块之间相互协作来完成软件开发。

- 什么B/S和C/S

BS即Browser/Server(浏览器/服务器)结构，就是只安装维护一个服务器，而客户端采用浏览器运行软件。

CS即Client/Server(客户端/服务器)，开发维护成本高于bs。因为采用CS结构时，对于不同的客户端要开发不同的程序，而且软件安装调试和升级都需要在所有客户机上进行。

## 2. MVC
[MVC](https://baike.baidu.com/item/MVC)全名是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。MVC被独特的发展起来用于映射传统的输入、处理和输出功能在一个逻辑的图形化用户界面的结构中。

MVC框架的核心思想是：**解耦**

**Model（模型）**是应用程序中用于处理应用程序数据逻辑的部分。
　　通常模型对象负责在数据库中存取数据。

**View（视图）**是应用程序中处理数据显示的部分。
　　通常视图是依据模型数据创建的。

**Controller（控制器）**是应用程序中处理用户交互的部分。
　　通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

当前主流的开发语言如Java、PHP、Python中都有MVC框架。

![选区_236](3. Web MVC各部分的功能

**M**全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。

**V**全拼为View，用于封装结果，生成页面展示的html内容。

**C**全拼为Controller，用于接收请求，处理业务逻辑，与Model和View交互，返回结果。

![](http://tp.jikedaohang.com/20191112223723_zM03Kp_Screenshot.jpeg)

## 4. Django简介
Django是一个开放[源代码](https://baike.baidu.com/item/源代码/3814213)的Web应用框架，由[Python](https://baike.baidu.com/item/Python/407313)写成。采用了MTV的框架模式，即模型M，视图V和模版T。它最初是被开发来用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站的，即是CMS（内容管理系统）软件。并于2005年7月在BSD许可证下发布。这套框架是以比利时的吉普赛爵士吉他手Django Reinhardt来命名的。

[点击查看:django官方网站](https://www.djangoproject.com/)

[点击查看:django源码](https://github.com/django/django)

[点击查看:2.0官方中文文档](https://docs.djangoproject.com/zh-hans/2.0/)

[点击查看:版本信息](https://www.djangoproject.com/download/)

**Django框架遵循MVC设计**，并且有一个专有名词：**MVT**



## 5. MVT各部分的功能

**M全拼为Model**，与MVC中的M功能相同，负责和数据库交互，进行数据处理。

**V全拼为View**，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。

**T全拼为Template**，与MVC中的V功能相同，负责封装构造要返回的html。

![](http://tp.jikedaohang.com/20191112224613_yjtN9m_Screenshot.jpeg)

##6. 协议

 - HTTP

   是互联网上应用最为广泛的一种网络协议，是一个客户端和服务器端请求和应答的标准（TCP），用于从WWW服务器传输超文本到本地浏览器的传输协议，它可以使浏览器更加高效，使网络传输减少。

- HTTPS

  是以安全为目标的HTTP通道，简单讲是HTTP的安全版，即HTTP下加入SSL层，HTTPS的安全基础是SSL，因此加密的详细内容就需要SSL。