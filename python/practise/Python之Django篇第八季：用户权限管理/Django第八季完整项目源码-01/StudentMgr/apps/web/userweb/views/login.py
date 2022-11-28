# ========= 引入基础的模块 ========
from resources_base.module_base.basetools import md5
from resources_base.module_base.importmodules import *
from web.rabcweb.services import init_permission_menu
# ========= 导入数据模块 ==========
from userweb.models import Account, Permission


def index(request):
    """返回登陆页面"""
    return render(request, 'user/login.html')


"""
def demo_login(request):
    # 取出cookid
    username = request.session.get('username',"")
    password = request.session.get('password',"")
    return render(request,'user/demo_login.html', context={'username': username, 'password': password})


def set_cookie(request):
    # 获取用户名和密码
    loginid = request.POST.get('loginid')
    loginpwd = request.POST.get('loginpwd')
    # 实例化一个HttpReponse
    res = HttpResponse()
    # 设置cookie
    res.set_cookie('username', loginid, max_age=14*24*3600)
    res.set_cookie('password', loginpwd, expires=datetime.now() + timedelta(days=14))
    # 返回给用户
    return res

def set_session(request):
    # 获取用户名和密码
    loginid = request.POST.get('loginid')
    loginpwd = request.POST.get('loginpwd')
    # 定义一个res
    res = HttpResponse("Session设置完成！")
    # 设置cookie
    request.session['username']=loginid
    request.session['password'] = loginpwd
    request.session.set_expiry(30*3600)
    # 返回给用户
    return res


def flush_session(request):
    request.session.flush()
    return HttpResponse("Session已被清除！")
"""


def login_handle(request):
    """处理用户登陆"""
    # 接收前端传递的数据
    loginid = request.POST.get('loginid')
    loginpwd = request.POST.get('loginpwd')
    # 使用异常处理
    try:
        # ==== 根据loginId获取用户 =====
        obj_users = Account.objects.filter(Q(loginid=loginid) | Q(mobile=loginid) | Q(email=loginid))
        # 判断是否存在
        if not obj_users:
            return JsonResponse({'code': 1, 'error': '登陆的用户信息不存在！'})
        # 判断是否禁用
        if not obj_users[0].status:
            return JsonResponse({'code': 2, 'error': '账号已禁用，请联系管理员！'})

        # 验证密码
        obj_user = obj_users.filter(loginpwd=md5(loginpwd)).first()
        # 判断是否存在
        if not obj_user:
            return JsonResponse({'code': 3, 'error': '密码错误！'})
        # ======== 登陆成功，写入当前的时候 ===========
        obj_user.last_login = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obj_user.save()
        # ===== 获取返回数据 ====
        res_data = {
            'loginid': obj_user.loginid, 'name': obj_user.name,
            'department': obj_user.department, 'position': obj_user.position,
            'mobile': obj_user.mobile, 'email': obj_user.email,
            'create_time': obj_user.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            'last_login': obj_user.last_login
        }
        # === 添加修改时间 ==
        if obj_user.edit_time:
            res_data['edit_time'] = obj_user.edit_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            res_data['edit_time'] = "尚未修改"
        # ===存储到session===
        request.session['user'] = res_data
        # ======== 获取权限并构建菜单========
        init_permission_menu.init_data(request, obj_user)
        # ======= 返回当前的id和name ======
        return JsonResponse({'code': 0})

    except Exception as e:
        return JsonResponse({'code': 4, 'error': '身份验证出现异常，具体原因:' + str(e)})
