# ========= 引入基础模块 ===========
from resources_base.module_base.importmodules import *
# ========= 引入数据models类 ============
from basicweb.models import Faculty


def index(request):
    return render(request, 'basic/faculty.html')


def list_values(request):
    """获取院系的数据"""
    # 接收查询的条件
    q_str = request.POST.get('queryStr', "")

    # 准备SQL语句
    sql = """
    Select T3.Id,T3.Name, Count(T3.id2) As 'Number' 
    From 
    (
        Select T1.Id, T1.Name, T2.Id As "id2"
        from Basic_Faculty As T1
        Left Join Basic_Major As T2 On T1.id = T2.faculty_id
			  where T1.Name Like '%s'
    ) AS T3
    Group By T3.Id,T3.Name
    """ % ('%' + q_str + '%')
    # 开始执行
    response = sqlhelper.get_db_data_dict(sql, ['id', 'name', 'number'])
    # 判断
    if response['status']:
        # 返回
        return JsonResponse({'status': True, 'data': response['data']})
    else:
        return JsonResponse({'status': False, 'error': response['error']})


def add_value(request):
    """添加"""
    # 接收传递过来的名称
    name = request.POST.get('name')
    try:
        # 写入数据库
        Faculty.objects.create(name=name)
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': "写入数据库出现异常，具体原因：" + str(e)})


def edit_value(request):
    """修改"""
    # 获取传递过来的数据
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    # 修改
    try:
        obj = Faculty.objects.get(id=id)
        obj.name = name
        obj.save()
        return JsonResponse({'status': True })
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改提交到数据库出现异常，具体原因：' + str(e)})


def del_value(request):
    """删除"""
    # 获取Id
    id = request.POST.get('id')
    # 删除
    try:
        Faculty.objects.get(id=id).delete()
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '删除提交到数据库出现异常！具体原因：' + str(e)})
