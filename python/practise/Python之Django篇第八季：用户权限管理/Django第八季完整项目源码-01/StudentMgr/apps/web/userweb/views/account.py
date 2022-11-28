# ========= 引入基础的模块 ========
from resources_base.module_base.importmodules import *
from resources_base.module_base.basetools import md5
# ========= 导入数据模块 ==========
from userweb.models import Account, Roles


def index(request):
    return render(request, 'user/account.html')


def list_values(request):
    """获取所有的登陆账号"""
    # 接收前台传递的数据
    page = int(request.POST.get('page'))
    limit = int(request.POST.get('limit'))
    q_str = request.POST.get('q_str')
    q_status = request.POST.get('q_status')
    q_department = request.POST.get('q_department')
    # 获取所有的登陆账号
    obj_accounts = list(Account.objects.filter(Q(loginid__icontains=q_str) | Q(name__icontains=q_str)).
                        filter(status__icontains=q_status, department__icontains=q_department).values())
    # 分页
    one_page_data = obj_accounts[(page - 1) * limit: page * limit]
    # 优化展示
    for index, value in enumerate(one_page_data):
        # 获取角色信息 --- 为xmselect下拉框提供数据
        roles_obj = list(Roles.objects.filter(account__loginid=value.get('loginid')).values("id",'name'))
        # 定义变量
        roles_select = []
        # 遍历
        for item in roles_obj:
            roles_select.append({'name': item.get('name'), 'value': item.get('id')})
        # ==== 附加到返回的数据中 ===
        one_page_data[index]['selected_roles'] = roles_select
        # 创建时间的格式
        if value.get('create_time'):
            one_page_data[index]['create_time'] = value.get('create_time').strftime("%Y-%m-%d %H:%M:%S")
        # 修改时间的格式
        if value.get('edit_time'):
            one_page_data[index]['edit_time'] = value.get('edit_time').strftime("%Y-%m-%d %H:%M:%S")
        # 上次登陆时间的格式
        if value.get('last_login'):
            one_page_data[index]['last_login'] = value.get('last_login').strftime("%Y-%m-%d %H:%M:%S")
        else:
            one_page_data[index]['last_login'] = "尚未登陆"

    # 返回
    return JsonResponse({'code': 0, 'count': len(obj_accounts), 'data': one_page_data})


def add_value(request):
    """添加账号"""
    # 接收传递的值
    rec = request.POST
    # 获取角色的字符串
    roles_str = rec.get('roles')
    # 定义返回值
    res = {'status': True}
    # 判断登陆账号是否存在
    is_exists = Account.objects.filter(loginid=rec.get('loginid')).exists()
    # 判断
    if is_exists:
        res['status'] = False
        res['error'] = "登陆账号已存在！"
    else:

        try:
            # =========== 第一步：添加登录账号 ===============
            Account.objects.create(
                loginid=rec.get('loginid'),
                loginpwd=md5(rec.get('loginpwd')),
                status=1 if (rec.get('status') == "on") else 0,
                name=rec.get('name'),
                department=rec.get('department'),
                position=rec.get('position'),
                mobile=rec.get('mobile'),
                email=rec.get('email'),
                create_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

            # =========== 第二部，添加账号和角色的映射关系 =============
            if roles_str:
                # 1) 获取当前的账号对象 ！
                account_obj = Account.objects.filter(loginid=rec.get('loginid')).first()
                # 2) 获取对应的角色
                roles_list = roles_str.split(",")
                # 遍历
                for item in roles_list:
                    # 获取响应的角色对象
                    roles_obj = Roles.objects.filter(id=int(item)).first()
                    # 添加映射
                    roles_obj.account.add(account_obj)
        except Exception as e:
            res['status'] = False
            res['error'] = "添加账号写入数据库出现异常，具体原因：" + str(e)
    # 返回
    return JsonResponse(res)


@csrf_exempt
def edit_value(request):
    """修改登陆账号"""
    # 接收传递的值
    rec = request.POST
    # 定义返回值
    res = {'status': True}
    # 开始修改
    try:
        # ============================ 步骤01:编辑除角色外的属性信息 =======================

        # ===获取当前账号===
        obj = Account.objects.filter(loginid=rec.get('loginid')).first()
        # ===修改相应的属性
        obj.name = rec.get('name')
        obj.department = rec.get('department')
        obj.position = rec.get('position')
        obj.status = 1 if (rec.get('status') == "on") else 0
        obj.mobile = rec.get('mobile')
        obj.email = rec.get('email')
        obj.edit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # ===保存====
        obj.save()

        # ========================== 步骤02:编辑角色外的属性信息 ============================
        # 1. 获取数据中记录的当前用户的角色
        db_roles = list(Roles.objects.filter(account__loginid=rec.get('loginid')).values_list('id', flat=True))

        # 2. 获取提交的时候角色信息
        commit_roles = []
        # 判断提交的是否为空
        if rec.get('roles'):
            roles_list = rec.get('roles').split(',')
            # 遍历
            for item in roles_list:
                commit_roles.append(int(item))

        # ==== 获取要删除的角色====
        del_roles = list(set(db_roles) - set(commit_roles))
        # ==== 获取要添加的角色 ===
        add_roles = list(set(commit_roles) - set(db_roles))

        # ==== 开始删除 ====
        for item in del_roles:
            # 实例化roles
            roles_obj = Roles.objects.filter(id=item).first()
            # 删除
            roles_obj.account.remove(obj)
        # ==== 开始添加 ====
        for item in add_roles:
            # 实例化roles
            roles_obj = Roles.objects.filter(id=item).first()
            # 删除
            roles_obj.account.add(obj)


    except Exception as e:
        res['status'] = False
        res['error'] = "修改账号写入数据库出现异常，具体原因：" + str(e)
    # 返回
    return JsonResponse(res)


def del_value(request):
    """删除账号"""
    # 接收数据
    rec = request.POST
    # 定义返回数据结构
    res = {'status': True}
    # 开始修改
    try:
        obj = Account.objects.filter(loginid=rec.get('loginid')).first()
        obj.delete()
    except Exception as e:
        res['status'] = False
        res['error'] = "删除账号写入数据库出现异常，具体原因：" + str(e)

    # 返回
    return JsonResponse(res)


def change_pass(request):
    """修改密码"""
    # 接收传递数据
    rec = request.POST
    # 定义返回的数据卷积核
    res = {'status': True}
    # 异常处理
    try:
        # 获取当前登陆账号
        obj = Account.objects.filter(loginid=rec.get('ch_loginid')).first()
        # 判断旧密码是否正确
        if obj.loginpwd != md5(rec.get('ch_oldPass')):
            res['status'] = False
            res['error'] = "旧密码输入错误！"
        else:
            obj.loginpwd = md5(rec.get('ch_newPass'))
            obj.edit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            obj.save()
    except Exception as e:
        res['status'] = False
        res['error'] = "修改密码写入数据库出现异常，具体原因：" + str(e)

    # 返回
    return JsonResponse(res)


def change_status(request):
    """修改用户的状态"""
    # 接收数据
    rec = request.POST
    # 定义返回数据结构
    res = {'status': True}
    # 开始修改
    try:
        obj = Account.objects.filter(loginid=rec.get('loginid')).first()
        # 修改状态
        obj.status = rec.get('status')
        # 保存
        obj.save()
    except Exception as e:
        res['status'] = False
        res['error'] = "添加账号写入数据库出现异常，具体原因：" + str(e)

    # 返回
    return JsonResponse(res)
