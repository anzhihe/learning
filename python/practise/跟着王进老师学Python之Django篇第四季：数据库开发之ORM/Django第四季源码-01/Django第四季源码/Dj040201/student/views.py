from django.shortcuts import render,reverse,redirect
from . import models
from django.http import HttpResponse


# Create your views here.

# ============== 从文件读取学员信息 ========
FILE_STU_NUMBER = [] # 比如：【30,17,13】
FILE_STUS = []  # 所有学生明细

# 读取文件数据
def read_student_from_file(path:str):
    """
    从文件中读取学生信息
    数据如下： [{}{}{}{}{}]
    :return: 
    """
    # 清空变量
    FILE_STUS.clear()
    # 定义男女生变量
    male_number = 0
    female_number = 0

    infos = ['sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address']
    # 读取
    try:
        with open(path, mode='r', encoding='utf-8-sig') as fd:
            current_line = fd.readline()
            while current_line:
                # 切分属性信息
                student = current_line.strip().replace("\n","").split(",")
                # 定义临时集合
                temp_student = {}
                for index in range(len(infos)):
                    temp_student[infos[index]] = student[index]
                # 附加到集合中
                FILE_STUS.append(temp_student)
                # 判断是男生还是女生
                if  "男" in temp_student["gender"]:
                    male_number += 1
                else:
                    female_number += 1
                # 读取下一行
                current_line = fd.readline()

            # 返回
            # return students
            student_number = len(FILE_STUS)

            # 写入到全局变量中
            FILE_STU_NUMBER.clear()
            FILE_STU_NUMBER.append(student_number)
            FILE_STU_NUMBER.append(male_number)
            FILE_STU_NUMBER.append(female_number)

    except Exception as e:
        print("读取文件出现异常，具体为：" + str(e))


def index(request):
    if request.method == "GET":
        # 在数据库中取数据
        students = models.Student.objects.all()
        # 展示在页面中
        return render(request, 'index.html', context={'students':students})
    if request.method == "POST":
        sno = request.POST.get('sno')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        # 把查询的输入的值带入页面
        query_list = []
        query_list.append(sno)
        query_list.append(name)
        query_list.append(mobile)
        query_list.append(email)

        # 获取满足条件的
        students = models.Student.objects.filter(sno__icontains=sno,
                                                 name__icontains=name,
                                                 mobile__icontains=mobile,
                                                 email__icontains=email)
        # 返回结果并展示
        return render(request,'index.html',context={'students':students, 'query':query_list})



def view(request):
    # 获取点击的学号
    sno = request.GET.get('sno')
    # 查询相应学号的学生信息
    student = models.Student.objects.get(sno=sno)
    # 展示明细页面
    return render(request, 'view.html', context={'student':student})

def add(request):
    # 添加单个学生
    if request.method == 'GET':
        return render(request, 'add.html')

    elif request.method == 'POST':
        # 获取提交的数据
        current_student = models.Student(sno=request.POST.get('sno'),
                                         name=request.POST.get('name'),
                                         gender=request.POST.get('gender'),
                                         birthday=request.POST.get('birthday'),
                                         mobile=request.POST.get('mobile'),
                                         email =request.POST.get('email'),
                                         address=request.POST.get('address'),
                                         )
        # 保存
        current_student.save()
        # 跳转到首页
        return redirect(reverse('index'))

def add_many(request):
    # 文件导入多个学生
    if request.method == "GET":
        return render(request, 'addmany.html')
    if request.method == "POST":
        # 遍历集合
        for student in FILE_STUS:
            current_student = models.Student(sno=student['sno'],name=student['name'], gender=student['gender'],
                                             birthday=student['birthday'], mobile=student['mobile'], email=student['email'],
                                             address=student['address']
                                             )
            current_student.save()
        # 跳转到首页
        return redirect(reverse('index'))



def read(request):
    # 获取文件的路径
    path = request.GET.get('path')
    # 调用读取文件的防范
    read_student_from_file(path)
    # 拼接字符串
    info = "总人数：" + str(FILE_STU_NUMBER[0]) + "\n" + "男生：" + str(FILE_STU_NUMBER[1])  + "\n" +"女生：" + str(FILE_STU_NUMBER[2])
    # 展示文件信息
    return render(request, 'addmany.html', context={'info':info,'path':path})
def delete(request):
    # 获取要删除学生的学号
    sno = request.GET.get('sno')
    # 获取这个对象信息
    current_student = models.Student.objects.get(sno=sno)
    # 删除
    current_student.delete()
    # 跳转到首页
    return redirect(reverse('index'))

def modify(request):

    # 判断方法
    if request.method == "GET":
        # 获取点击的学号
        sno = request.GET.get('sno')
        # 查询相应学号的学生信息
        student = models.Student.objects.get(sno=sno)
        # 展示明细页面
        return render(request, 'modify.html', context={'student': student})

    elif request.method == "POST":
        # 获取POST提交的值
        sno = request.POST.get('sno')

        # 获取当前学号的学生信息
        current_student = models.Student.objects.get(sno=sno)
        # 修改其他属性
        current_student.name = request.POST.get('name')
        current_student.gender = request.POST.get('gender')
        current_student.birthday = request.POST.get('birthday')
        current_student.mobile = request.POST.get('mobile')
        current_student.email = request.POST.get('email')
        current_student.address = request.POST.get('address')
        # 保存
        current_student.save()
        # 返回
        return redirect(reverse('index'))


