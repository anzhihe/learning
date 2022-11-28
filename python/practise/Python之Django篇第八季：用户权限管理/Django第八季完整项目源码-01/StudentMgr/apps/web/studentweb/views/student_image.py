# ========= 引入基础模块 ===========
from resources_base.module_base.importmodules import *
from resources_base.module_base.myupload import upload_file
# ========= 引入数据类 =============
from studentweb.models import StudentImage


def index(request):
    """学生照片的首页"""
    return render(request, 'student/student_image.html')


def list_value(request):
    """获取所有的照片"""
    # 接收查询提交
    rec = request.POST
    # 获取分页的两个变量
    page = int(request.POST.get('page'))
    limit = int(request.POST.get('limit'))
    # 定义两个日期
    start_time = ""
    end_time = ""
    # 把接收的字符串转为日期
    if rec.get('q_start'):
        start_str = rec.get('q_start').split("-")
        start_time = datetime(year=int(start_str[0]), month=int(start_str[1]), day=int(start_str[2]), hour=0, minute=0,
                              second=0)
    if rec.get('q_end'):
        end_str = rec.get('q_end').split("-")
        end_time = datetime(year=int(end_str[0]), month=int(end_str[1]), day=int(end_str[2]), hour=23, minute=59,
                            second=59)
    # 获取数据
    # === 1. 通过q_str筛选
    objs = StudentImage.objects.filter(
        Q(name__icontains=rec.get('q_str')) | Q(remark__icontains=rec.get('q_str'))).order_by('-create_time')
    # === 2. 开始时间和结束之间筛选
    if start_time and end_time:
        objs = objs.filter(create_time__gte=start_time, create_time__lte=end_time)
    # === 3. values --list
    objs = list(objs.order_by('-create_time').values())
    # 遍历
    for index, value in enumerate(objs):
        # 添加图片路径
        objs[index]['url'] = settings.MEDIA_URL + 'images' + os.path.sep + value.get('name')
        # 添加日期
        objs[index]['date'] = value.get('create_time').strftime("%Y-%m-%d")

    # 实现分页
    one_page_data = objs[(page - 1) * limit: page * limit]

    # 返回
    return JsonResponse({'code':1, 'count': len(objs), 'data': one_page_data})


def edit_value(request):
    """添加标注"""
    # 接收数据
    rec = request.POST
    # 开始修改
    obj = StudentImage.objects.filter(id=rec.get('id')).first()
    obj.remark = rec.get('remark')
    obj.save()
    # 返回
    return JsonResponse({'status': True})


def del_value(request):
    """删除照片"""

    # 接收要删除的id
    id = request.POST.get('id')
    # 定义返回的数据类型
    res = {'status': True}
    # 查询到要删除的对象
    obj = StudentImage.objects.filter(id=id).first()

    # ==== 1. 删除文件  ======
    file_name = settings.MEDIA_ROOT + os.path.sep + 'images' + os.path.sep + obj.name
    # 判断是否存在
    if os.path.exists(file_name):
        try:
            os.remove(file_name)
        except Exception as e:
            res['status'] = False
            res['error'] = "删除文件出现异常，具体原因：" + str(e)

    # ====2. 删除记录 ===========
    try:
        StudentImage.objects.filter(id=id).delete()
    except Exception as e:
        res['status'] = False
        res['error'] = "删除数据库记录出现异常，具体原因：" + str(e)

    return JsonResponse(res)


def upload(request):
    """实现图片的上传"""
    # 接受传递过来的文件
    rev_image = request.FILES.get('file')
    path = "images"
    # 调用后台通用模块写入文件
    response = upload_file(rev_image, path, type=1)
    # 如果写入文件正确，继续把文件信息写入到数据库
    if response.get('status'):
        # 写入数据库
        try:
            StudentImage.objects.create(name=response.get('data'), remark="",
                                        create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except Exception as e:
            response['status'] = False
            response['error'] = "文件信息写入数据库出现异常，具体原因：" + str(e)
    return JsonResponse(response)
