# ========= 引入基础的模块 ========
from resources_base.module_base.importmodules import *
from resources_base.module_base.basetools import md5
# ==========导入数据模块=========
from userweb.models import Account
# ==========引入邮件模块和redis模块=====
from django_redis import get_redis_connection
from django.core.mail import send_mail


def index(request):
    """展示页面"""
    return render(request, 'user/resetpass.html')


def get_account(request):
    """获取账号信息"""
    # 获取用户输入的信息
    input_str = request.POST.get('input_str')
    # 获取对象
    account_obj = Account.objects.filter(Q(loginid=input_str) | Q(email=input_str) | Q(mobile=input_str)).first()
    # 判断是否存在
    if not account_obj:
        return JsonResponse({'status': False, 'error': "当前输入的账号信息不存在！"})
    # 返回
    return JsonResponse(
        {'status': True,
         'data': {'loginid': account_obj.loginid, 'name': account_obj.name, 'email': account_obj.email}})


def send_email(request):
    """发送邮件"""
    # 接收前台传递的值
    email = request.POST.get('email')
    send_list = []
    send_list.append(email)
    # 生成验证码-- 6位随机数
    code = random.randint(100000, 999999)
    # 准备邮件内容
    email_title = "找回密码的邮件"
    email_body = "当前验证码：" + str(code) + "\n 【注意：当前验证码有效期15分钟，请尽快完成更改密码】"
    # 发送邮件
    try:
        # 发送
        res = send_mail(email_title, email_body, '651205558@qq.com', send_list)
        # 判断
        if res == 1:
            # === 把验证码写入缓存 ====
            redis_obj = get_redis_connection()
            redis_obj.set(email, code, 9000)
            # 返回
            return JsonResponse({'status': True})
        else:
            JsonResponse({'status': False, 'error': "当前邮件发送失败"})

    except Exception as e:
        return JsonResponse({'status': False, 'error': "当前邮件发送失败，具体原因：" + str(e)})


def check_code(request):
    """校验验证码"""
    # 获取传递的信息
    email = request.POST.get('email')
    input_code = request.POST.get('code')
    # 先去redis获取code
    redis_obj = get_redis_connection()
    redis_code = redis_obj.get(email)
    # 判断是否为空
    if not redis_obj:
        return JsonResponse({'status': False, 'error': "验证码已过期，请重新后去"})

    # 判断是否一样
    if input_code != redis_code.decode('utf-8'):
        return JsonResponse({'status': False, 'error': "验证码输入错误！"})

    return JsonResponse({'status': True})


def change_pass(request):
    """修改密码"""
    # 获取
    loginid = request.POST.get('loginid')
    newpass = request.POST.get('newpass')
    # 获取对象
    account_obj = Account.objects.filter(loginid=loginid).first()
    # 开始修改
    try:
        account_obj.loginpwd = md5(newpass)
        account_obj.save()
        return JsonResponse({'status': True})
    except Exception as e:
        return JsonResponse({'status': False, 'error': "修改密码出现异常，具体原因：" + str(e)})