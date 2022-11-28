# ========= 引入基础模块 ===========
from resources_base.module_base.importmodules import *
# ========= 引入数据models类 ============
from basicweb.models import Faculty, Major
from studentweb.models import Student


def index(request):
    return render(request, 'student/student.html')


def list_values(request):
    """获取数据"""
    # 获取分页的page和limit
    page = int(request.POST.get('page', 0))
    limit = int(request.POST.get('limit', 0))
    # 查询的条件获取
    q_sno_name = request.POST.get('q_sno_name')  # 模糊查询学号 or 模糊查询姓名
    q_faculty = request.POST.get('q_faculty')  # 匹配院系信息
    q_major = request.POST.get('q_major')  # 匹配专业信息
    q_status = request.POST.get('q_status')  # 匹配学生状态

    # 第一次过滤： -- 模糊查询学号 or 模糊查询姓名
    filter_data = Student.objects.filter(Q(sno__icontains=q_sno_name) | Q(name__icontains=q_sno_name))

    # 第二次过滤： -- 匹配院系信息
    if len(q_faculty) > 0:
        filter_data = filter_data.filter(faculty_id = q_faculty)

    # 第三次过滤： -- 匹配专业信息
    if len(q_major) > 0:
        filter_data = filter_data.filter(major_id=q_major)

    # 第四次过滤： -- 匹配学生状态
    if q_status == 'true':
        filter_data = filter_data.filter(status__icontains='在校')

    # 处理数据：list --- values()
    objs = list(filter_data.values('sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address',
                                   'major','major__name', 'faculty','faculty__name', 'start_date', 'status'))
    # 定义一个返回的数据集
    res = {'code': 0, 'count': len(objs), 'data': objs}

    # 判断是否收到page和limit
    if page != 0 and limit != 0:
        one_page_data = objs[(page - 1) * limit: page * limit]
        res['data'] = one_page_data

    return JsonResponse(res)


def is_sno_exists(request):
    """校验学号是否存在"""
    # 获取学号
    sno = request.POST.get('sno')
    # 判断
    is_exists = Student.objects.filter(sno=sno).exists()
    # 返回
    return JsonResponse({'data': is_exists})


def add_value(request):
    """完成学生信息的添加"""
    # 接收传递的值
    rec = request.POST
    # 添加
    try:
        Student.objects.create(sno=rec['sno'], name=rec['name'], gender=rec['gender'], birthday=rec['birthday'],
                               mobile=rec['mobile'], email=rec['email'], address=rec['address'],
                               faculty= Faculty.objects.get(id=rec['faculty']),
                               major = Major.objects.get(id=rec['major']), start_date=rec['start_date'],
                               status = rec['status'])
        return JsonResponse({'status':True})
    except Exception as e:
        return JsonResponse({'status':False, 'error': '添加学生提交到数据库出现异常，具体原因：' + str(e)})


def edit_value(request):
    # 接收传递的值
    rec = request.POST
    # 修改
    try:
        # 获取当前的对象
        obj = Student.objects.get(sno=rec['sno'])
        # 逐一修改属性
        obj.name = rec.get('name')
        obj.gender = rec['gender']
        obj.birthday = rec['birthday']
        obj.mobile = rec['mobile']
        obj.email = rec['email']
        obj.address = rec['address']
        obj.faculty = Faculty.objects.get(id=rec['faculty'])
        obj.major = Major.objects.get(id=rec['major'])
        obj.start_date = rec['start_date']
        obj.status = rec['status']
        # 保存
        obj.save()
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改学生信息提交到数据库出现异常，具体原因：' + str(e)})


def del_value(request):
    # 接收传递的值
    sno = request.POST.get('sno')
    # 修改
    try:
        # 获取当前的对象并删除
        Student.objects.get(sno=sno).delete()

        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改学生信息提交到数据库出现异常，具体原因：' + str(e)})
