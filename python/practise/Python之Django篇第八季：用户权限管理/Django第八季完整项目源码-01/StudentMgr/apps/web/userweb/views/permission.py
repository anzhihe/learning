# ========= 引入基础的模块 ========
from resources_base.module_base.importmodules import *
# ========= 引入数据信息 ========
from userweb.models import Menu, Permission


def index(request):
    """角色管理页面"""
    return render(request, 'user/permission.html')


def list_values(request):
    """获取所有权限的信息"""
    # 获取所有的menu信息
    obj_menus = list(Menu.objects.all().values().order_by('order'))
    # 获取所有的permission信息
    obj_permission = list(Permission.objects.all().values().order_by('order'))
    # =========== 组合成需要的数据样式 ===========
    data = []
    # 遍历menu
    for item in obj_menus:
        # 定义一个临时的字典
        temp_dict = {}
        # 添加id和title
        temp_dict['id'] = item.get('id')
        temp_dict['title'] = item.get('title')
        temp_dict['spread'] = True
        # 定义children为list集合
        temp_dict['children'] = []
        # === 遍历权限 ===
        for val in obj_permission:
            # 判读权限是否属于当前菜单
            if val.get('menu_id') == item.get('id'):
                # 添加到temp_dict的children的list中
                temp_dict['children'].append({'id': val.get('order'), 'title': val.get('title'),
                                              'url': val.get('url'), 'node_id': val.get('id'),
                                              'p_id': item.get('id'), 'p_title': item.get('title')})

        # 附加到data中
        data.append(temp_dict)

    # ==== 返回===
    return JsonResponse({'data': data}, json_dumps_params={"ensure_ascii": False})


def add_value(request):
    """实现权限条目的添加"""
    # 接收前台数据
    rec = request.POST
    # 判断title,url,order是否重复
    is_exists = Permission.objects.filter(Q(title__icontains=rec.get('title'))|
                                          Q(url__icontains=rec.get('url'))|
                                          Q(order = int(rec.get('order')))).exists()
    if is_exists:
        return JsonResponse({'status': False, 'error': '标题、URL或者order已存在！'})

    try:
        Permission.objects.create(title=rec.get('title'), url=rec.get('url'), order=rec.get('order'), menu_id=rec.get('menu'))
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '添加权限条目出现异常！具体原因：' + str(e)})


def edit_value(request):
    """实现权限条目的修改"""
    # 接收前台数据
    rec = request.POST
    # 开始修改
    try:
        # 获取对象
        obj = Permission.objects.get(id=rec.get('id'))
        # 逐一修改
        obj.title = rec.get('title')
        obj.url = rec.get('url')
        obj.menu_id = rec.get('menu')
        obj.order = rec.get('order')
        # 保存
        obj.save()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改权限条目出现异常！具体原因：' + str(e)})


def del_value(request):
    """实现权限条目的删除"""
    # 开始删除
    try:
        # 获取对象并删除
        Permission.objects.get(id=request.POST.get('id')).delete()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '删除权限条目出现异常！具体原因：' + str(e)})
