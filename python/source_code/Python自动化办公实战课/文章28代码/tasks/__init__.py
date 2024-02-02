from __future__ import absolute_import # 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from celery import Celery

# 创建celery应用对象
app = Celery("tasks")

# 导入celery的配置信息
app.config_from_object("tasks.config")


