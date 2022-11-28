# ========= 引入基础的模块 ========
from resources_base.module_base.importmodules import *
# ========= 引入数据类 ============
from userweb.models import Menu


def index(request):
    """角色管理页面"""
    return render(request, 'user/menu.html')


def list_values(request):
    """获取所有的菜单信息"""
    # 获取查询的字符串
    q_str = request.POST.get('q_str',"")
    # 获取对象
    objs = list(Menu.objects.filter(title__icontains=q_str).values().order_by('order'))
    # 返回
    return JsonResponse({'status': True, 'data': objs})


def add_value(request):
    # 获取传递的值
    rec = request.POST
    # 判断是否存在
    is_exists = Menu.objects.filter(title__icontains=rec.get('title')).exists()
    if is_exists:
        return JsonResponse({'status': False, 'error': '当前菜单标题已存在！'})

    try:
        # 直接创建
        Menu.objects.create(title=rec.get('title'), icon=rec.get('icon'), order=rec.get('order'))
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '添加菜单出现异常，具体原因：' + str(e)})


def edit_value(request):
    # 获取传递的值
    rec = request.POST
    try:
        # 获取当前的对象
        obj = Menu.objects.get(id=rec.get('id'))
        # 修改
        obj.title = rec.get('title')
        obj.icon = rec.get('icon')
        obj.order = rec.get('order')
        # 保存
        obj.save()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改菜单出现异常，具体原因：' + str(e)})


def del_value(request):

    try:
        Menu.objects.filter(id=request.POST.get('id')).delete()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '删除菜单出现异常，具体原因：' + str(e)})


def list_for_select(request):
    """获取所有的菜单提供给xmselect [{'name':  value:}]"""
    # 获取所有的menu
    objs = list(Menu.objects.all().values('id','title'))
    # 定义一个集合
    data = []
    # 遍历
    for item in objs:
        data.append({'name': item.get('title'), 'value': item.get('id')})
    # 返回
    return JsonResponse({'data': data})