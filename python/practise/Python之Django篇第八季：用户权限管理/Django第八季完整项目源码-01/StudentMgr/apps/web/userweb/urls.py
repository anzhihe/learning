# ===== 引入path ======
from django.urls import path
# ===== 引入views  ======
from userweb.views import account as account_views
from userweb.views import login as login_views
from userweb.views import resetpass as resetpass_views
from userweb.views import roles as roles_views
from userweb.views import menu as menu_views
from userweb.views import permission as permission_views


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
    # ==== 角色管理 ========
    path('roles/', roles_views.index, name="roles"),
    path('roles/list/', roles_views.list_values, name="list_roles"),
    path('roles/add/', roles_views.add_value, name="add_roles"),
    path('roles/edit/', roles_views.edit_value, name="edit_roles"),
    path('roles/del/', roles_views.del_value, name="del_roles"),
    path('roles/select/', roles_views.get_roles_select, name="select_roles"),
    path('roles/update/permission/', roles_views.update_permission, name="update_roles_permission"),
    # ==== 菜单管理 ========
    path('menu/', menu_views.index, name="menu"),
    path('menu/list/', menu_views.list_values, name="list_menu"),
    path('menu/add/', menu_views.add_value, name="add_menu"),
    path('menu/edit/', menu_views.edit_value, name="edit_menu"),
    path('menu/del/', menu_views.del_value, name="del_menu"),
    path('menu/list/select/', menu_views.list_for_select, name="list_menu_select"),

    # ==== 权限管理 ========
    path('permission/', permission_views.index, name="permission"),
    path('permission/list/', permission_views.list_values, name="list_permission"),
    path('permission/add/', permission_views.add_value, name="add_permission"),
    path('permission/edit/', permission_views.edit_value, name="edit_permission"),
    path('permission/del/', permission_views.del_value, name="del_permission"),


]


# from userweb.views import demo as demo_views
# ==== redis测试 =========
# path("demo/set_redis/", demo_views.set_redis),
# path("demo/get_redis/", demo_views.get_redis),
# path('demo/send_mail/', demo_views.send_email),