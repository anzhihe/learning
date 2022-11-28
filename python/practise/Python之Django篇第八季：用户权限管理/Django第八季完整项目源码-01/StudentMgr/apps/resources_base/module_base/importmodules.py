# 引入常见的基础模块
from django.shortcuts import render, HttpResponse, redirect, reverse
# 插入Django.http中的模块
from django.http import JsonResponse, FileResponse
# 插入时间日期
from datetime import datetime, date, timedelta
# 插入Q,Sum
from django.db.models import Q, Sum
# 插入随机函数
import random
# 插入setting
from django.conf import settings
# 引入数据库通用类
from resources_base.module_base import sqlhelper
# 引入os模块
import os
# 引入uuid
import uuid
# csrf
from django.views.decorators.csrf import csrf_exempt
# json
import json