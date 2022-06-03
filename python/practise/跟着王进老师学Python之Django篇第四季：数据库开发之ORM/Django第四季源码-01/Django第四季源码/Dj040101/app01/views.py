from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):

    # 获取action值
    action = request.GET.get('action')

    # 根据action提供的值进行增删改查
    if action == 'add': # 添加
        # 添加张三
        zhangsan = models.Student(sno='95010', name='张三', gender='女', birthday='1990-04-05',
                                  mobile='13901234321', email='zhangsan@abc.com',
                                  address='上海市闵行区银都路122号')
        # 保存到数据库
        zhangsan.save()
        # 返回结果
        return render(request, 'index.html', context={'info': "数据添加成功！"})


    elif action == 'modify': # 修改
        # 把张三的性别改为男
        # 1. 获取张三的信息
        zhangsan = models.Student.objects.get(name='张三')
        # 2. 把性别改为男
        zhangsan.gender = '男'
        # 3. 保存修改
        zhangsan.save()
        # 返回给页面一个结果
        return render(request, 'index.html', context={'info': "数据修改成功！"})

    elif action == 'show': # 获取数据
        # 获取所有数据
        """
        students = models.Student.objects.all()
        str_student = ""
        for student in students:
            str_student += str(student)
        return render(request, 'index.html', context={'info': str_student})
        """
        # 展示某一个数据
        student = models.Student.objects.get(name='陈鹏')
        return render(request, 'index.html', context={'info': str(student)})

    elif action == 'delete': # 删除
        # 删除张三的信息
        # 1. 获取张三的信息
        zhangsan = models.Student.objects.get(name='张三')
        # 2. 删除
        zhangsan.delete()
        # 3. 返回前段提示
        return render(request, 'index.html', context={'info': "数据删除成功！"})

    else:
        return render(request, 'index.html')

