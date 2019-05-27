# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------------------
# models.py
#--------------------------------------------------------------------------
# auther:Liutiansi
# Email:liutiansi@gmail.com
#Blog:http://blog.liuts.com
# update:2010-11-03
#
#---------------------------------------------------------------------------

from django.db import models

"""
=数据库char类型类
-调用方法BetterCharField(长度)
"""
class BetterCharField(models.Field):
    def __init__(self, max_length, *args, **kwargs):
        self.max_length_value = max_length
        super(BetterCharField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length_value


"""
=主机表
"""
class Hostinfo(models.Model):
    ID = models.AutoField(primary_key=True,max_length=6)
    AppName =  BetterCharField(40)
    URL =  BetterCharField(100)
    IDC =  BetterCharField(3)
    Alarmtype = BetterCharField(8)
    Alarmconditions = BetterCharField(30)


"""
=监控结果表
"""
class MonitorData(models.Model):
    ID = models.AutoField(primary_key=True,max_length=6)
    FID = models.SmallIntegerField()
    NAMELOOKUP_TIME =  models.FloatField()
    CONNECT_TIME =  models.FloatField()
    PRETRANSFER_TIME =  models.FloatField()
    STARTTRANSFER_TIME =  models.FloatField()
    TOTAL_TIME =  models.FloatField()
    HTTP_CODE =  models.CharField(max_length=100)
    SIZE_DOWNLOAD =  models.FloatField()
    HEADER_SIZE =  models.SmallIntegerField()
    REQUEST_SIZE =  models.SmallIntegerField()
    CONTENT_LENGTH_DOWNLOAD=models.FloatField()
    SPEED_DOWNLOAD=models.FloatField()
    DATETIME=models.IntegerField(max_length=12)
    MARK=BetterCharField(1)
