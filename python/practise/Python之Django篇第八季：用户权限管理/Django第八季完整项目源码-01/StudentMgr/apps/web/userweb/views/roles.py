# ========= 引入基础的模块 ========
from resources_base.module_base.importmodules import *
# ========= 导入数据类 ============
from userweb.models import Roles, Permission


def index(request):
    """角色管理页面"""
    return render(request, 'user/roles.html')


def list_values(request):
    # 接收传递的值
    page = int(request.POST.get('page'))
    limit = int(request.POST.get('limit'))
    q_str = request.POST.get('q_str')
    # 获取符合条件的角色
    objs = list(Roles.objects.filter(name__icontains=q_str).values('id', 'name', 'desc'))
    # 分页
    one_page_data = objs[(page - 1) * limit: page * limit]
    # 为当前页中所有的角色获取其权限信息
    for index,value in enumerate(one_page_data):
        # 获取当前权限信息 --- [3,5,6]
        objs_permission = list(Permission.objects.filter(roles__id=value.get('id')).values_list('order', flat=True))
        # 添加到属性中
        one_page_data[index]['permissions'] = objs_permission
    # 返回
    return JsonResponse({'code': 0, 'count': len(objs), 'data': one_page_data})


def add_value(request):
    """实现角色的添加"""
    # 接收传递的值
    rec = request.POST
    # 判断是否存在
    is_exists = Roles.objects.filter(name=rec.get('name')).exists()
    # 如果存在
    if is_exists:
        return JsonResponse({'status': False, 'error': '角色名称已存在！'})

    # 开始添加
    try:
        Roles.objects.create(name=rec.get('name'), desc=rec.get('desc'))
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '添加角色信息出现异常，具体原因：' + str(e)})


def edit_value(request):
    """实现角色信息的修改"""
    # 接收传递的值
    rec = request.POST
    # 开始修改
    try:
        obj = Roles.objects.filter(id=rec.get('id')).first()
        # 修改
        obj.name = rec.get('name')
        obj.desc = rec.get('desc')
        # 保存
        obj.save()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改角色信息出现异常，具体原因：' + str(e)})


def del_value(request):
    """删除角色信息"""
    # 接收传递的信息
    rec = request.POST
    # 开始删除
    try:
        Roles.objects.filter(id=rec.get('id')).delete()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '删除角色信息出现异常，具体原因：' + str(e)})


def get_roles_select(request):
    """获取roles数据提供给xmselect"""
    # 定义一个变量
    roles_obj = []
    # 判断是什么方法
    if request.method == "GET":
        # 获取
        roles_obj = list(Roles.objects.all().values('id', 'name'))
    elif request.method == "POST":
        # 获取
        roles_obj = list(Roles.objects.filter(account__loginid=request.POST.get('loginid')).values('id', 'name'))
    # 定义一个集合
    roles_list = []
    # 遍历
    for item in roles_obj:
        roles_list.append({'name': item.get('name'), 'value': item.get('id')})

    # 返回
    return JsonResponse({'data': roles_list})


def update_permission(request):
    """更改角色的权限"""
    # 接收传递的值
    roles_id = request.POST.get('roles_id')
    commit_list = json.loads(request.POST.get('commit'))

    # 获取数据库中响应的存储角色的权限({},{},)
    db_list = list(Permission.objects.filter(roles__id=roles_id).values_list('id', flat=True))

    # 需要添加的权限
    add_list = list(set(commit_list) - set(db_list))
    # 需要删除的权限
    remove_list = list(set(db_list) - set(commit_list))

    # ==== 写入到数据库 ===
    try:
        # 1. 获取当前的角色对象
        roles_obj = Roles.objects.filter(id=roles_id).first()
        # 2. 删除
        for item in remove_list:
            # 实例化权限对象
            permission_obj = Permission.objects.filter(id=int(item)).first()
            # 删除
            permission_obj.roles.remove(roles_obj)

        # 3. 添加
        for item in add_list:
            # 实例化权限对象
            permission_obj = Permission.objects.filter(id=int(item)).first()
            # 删除
            permission_obj.roles.add(roles_obj)

        # 返回
        return JsonResponse({'status': True})

    except Exception as e:
        return JsonResponse({'status': False, 'error': '更改权限写入到数据库出现异常，具体原因：' + str(e)})
