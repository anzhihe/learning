# ========= 引入组件======
from userweb.models import Permission
from django.conf import settings


def init_data(request, obj_user):
    """
    根据当前用户信息获取权限和menu
    :param request: 客户端发起的request请求
    :param obj: 当前登录的用户对象
    :return:
    """
    # =========================== 登录后获取当前用户的权限以及菜单 ================================
    permission_queryset = list(Permission.objects.filter(roles__account__loginid=obj_user.loginid).values('id',
                                  'url','order','title','menu_id','menu__icon','menu__title','menu__order')
                               .order_by('menu__order', 'order').distinct())

    # ======= 任务1：构建当前用户拥有的权限列表=======
    permission_list = []
    # 遍历
    for item in permission_queryset:
        permission_list.append(item.get('url'))
    # 把Authed_WHITE_URL添加进去
    permission_list.extend(settings.AUTHED_WHITE_URL)
    print(permission_list)
    # ======= 任务2：构建当前用户登录后的侧边栏 =======
    # 方法01： 构建List集合
    """
    menu_list = []
    # 遍历
    for item in permission_queryset:
        # 判断是否为空
        if len(menu_list) == 0:
            # 定义一个新的dict
            temp_dict = {}
            temp_dict['id'] = item.get('menu_id')
            temp_dict['title'] = item.get('menu__title')
            temp_dict['icon'] = item.get('menu__icon')
            temp_dict['order'] = item.get('menu__order')
            temp_dict['children'] = [{'id': item.get('id'), 'title': item.get('title'), 'url': item.get('url'), 'order':item.get('order')}]
            # 附加到menu_list
            menu_list.append(temp_dict)
            # 第一条结束
            continue

        # 遍历ment_list判断是否存在当前的menu
        for index, value in enumerate(menu_list):
            if value.get('id') == item.get("menu_id"):
                menu_list[index]['children'].append({'id': item.get('id'), 'title': item.get('title'), 'url': item.get('url'), 'order':item.get('order')})
                break
            if index == len(menu_list)-1:
                # 定义一个新的dict
                temp_dict = {}
                temp_dict['id'] = item.get('menu_id')
                temp_dict['title'] = item.get('menu__title')
                temp_dict['icon'] = item.get('menu__icon')
                temp_dict['order'] = item.get('menu__order')
                temp_dict['children'] = [{'id': item.get('id'), 'title': item.get('title'), 'url': item.get('url'),
                                         'order': item.get('order')}]
                # 附加到menu_list
                menu_list.append(temp_dict)
    """
    # 方法02： 构建dict集合
    menu_dict = {}
    # 循环
    for item in permission_queryset:
        # 获取当前记录menu_id
        menu_id = item.get('menu_id')
        # 判断在menu_dict中menu_id是否存在
        if menu_id not in menu_dict:
            # 新产生一个
            menu_dict[menu_id] = {
                'title': item.get('menu__title'),
                'icon': item.get('menu__icon'),
                'order': item.get('menu__order'),
                'children': [
                    {
                        'id': item.get('id'),
                        'title': item.get('title'),
                        'url': item.get('url'),

                    }
                ]
            }
        else:
            menu_dict[menu_id]['children'].append({
                'id': item.get('id'),
                'title': item.get('title'),
                'url': item.get('url'),

            })

    # ========== 存储在session ============
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_dict