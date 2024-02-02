from __future__ import absolute_import # 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from celery.schedules import crontab

broker_url = "redis://127.0.0.1:6379/1"  

timezone = "Asia/Shanghai"  # 时区设置

# 导入任务所在文件
imports = [
    "tasks.jobs.test1",  # 导入py文件
    "tasks.jobs.test2",
]


# 需要执行任务的配置
beat_schedule = {
   "test1": {
        "task": "tasks.jobs.test1.run1",  #执行的函数
        "schedule": crontab(minute=1, hour=22, day_of_week=6),
        "args": ()
    }, 
   "test2": {
        "task": "tasks.jobs.test2.run1",  #执行的函数
        "schedule": crontab(minute="*"),
        "args": ()
    }, 

}
