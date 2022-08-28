# ===== 引入path ======
from django.urls import path
# ===== 引入views  ======
from userweb.views import account as account_views
from userweb.views import login as login_views
from userweb.views import resetpass as resetpass_views

# ==== 匹配当前app中的url===
urlpatterns = [
    # ==== 登陆账号 ====
    path('account/', account_views.index, name="account"),
    path('account/list/', account_views.list_values, name="list_account"),
    path('account/add/', account_views.add_value, name="add_account"),
    path('account/edit/', account_views.edit_value, name="edit_account"),
    path('account/del/', account_views.del_value, name="del_account"),
    path('account/chpwd/', account_views.change_pass, name="chpwd_account"),
    path('account/chstatus/', account_views.change_status, name="chstatus_account"),
    # === 登陆页面 ====
    path('login/', login_views.index, name="login"),
    path('login/handle/', login_views.login_handle, name="login_handle"),
    # ====重置密码 ===========
    path('reset/pass/', resetpass_views.index, name="reset_pass"),
    path('reset/pass/get_account/', resetpass_views.get_account, name="reset_pass_get_account"),
    path('reset/pass/send_email/', resetpass_views.send_email, name="reset_pass_send_email"),
    path('reset/pass/check_code/', resetpass_views.check_code, name="reset_pass_check_code"),
    path('reset/pass/commit/', resetpass_views.change_pass, name="reset_pass_commit"),
]


# from userweb.views import demo as demo_views
# ==== redis测试 =========
# path("demo/set_redis/", demo_views.set_redis),
# path("demo/get_redis/", demo_views.get_redis),
# path('demo/send_mail/', demo_views.send_email),