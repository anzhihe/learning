### API文档

DRF给我提供了自动生成API文档的功能，大大省去了写开发文档的时间。

```
pip install coreapi 
```

### 路由

```
from rest_framework.documentation import include_docs_urls
path('docs/', include_docs_urls(title='测试平台接口文档'))
```

