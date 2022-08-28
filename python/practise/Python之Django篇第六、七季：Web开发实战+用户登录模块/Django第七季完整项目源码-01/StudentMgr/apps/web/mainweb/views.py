# ========= 引入基础的模块 ========
from resources_base.module_base.importmodules import *
from resources_base.module_base.basetools import md5
# ==========导入数据模块=========
from userweb.models import Account


def index(request):
    """直接返回main页面 """
    return render(request, 'main/index.html')


def edit_value(request):
    """修改个人信息"""
    # 接收传递的值
    rec = request.POST
    # 修改
    try:
        # 获取当前用户
        obj = Account.objects.filter(loginid=rec.get('loginid')).first()
        # 逐一修改
        obj.name = rec.get('name')
        obj.department = rec.get('department')
        obj.position = rec.get('position')
        obj.email = rec.get('email')
        obj.mobile = rec.get('mobile')
        # 更新修改时间
        obj.edit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 保存
        obj.save()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改个人信息提交到数据库出现异常，具体原因：' + str(e)})


def change_pass(request):
    """修改密码"""
    # 获取传递的数据
    loginid = request.POST.get('ch_loginid')
    old_pass = request.POST.get('oldpwd')
    new_pass = request.POST.get('loginpwd')
    # 判断旧密码是否正确
    account_obj = Account.objects.filter(loginid=loginid, loginpwd=md5(old_pass)).first()
    if not account_obj:
        return JsonResponse({'status': False, 'error': '旧密码输入错误！'})

    # 修改
    try:
        # 修改
        account_obj.loginpwd = md5(new_pass)
        # 保存
        account_obj.save()
        # 返回
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': '修改密码提交到数据库出现异常，具体原因：' + str(e)})


def user_logout(request):
    """实现用户的注销"""
    # 清除当前session
    request.session.flush()
    # 跳转到登录页面
    return redirect(reverse('login'))