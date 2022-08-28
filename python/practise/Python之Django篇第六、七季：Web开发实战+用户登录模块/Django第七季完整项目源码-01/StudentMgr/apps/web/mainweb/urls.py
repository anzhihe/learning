from django.urls import path
# 引入当前app的views
from mainweb import views as main_views
# ==== 匹配当前app中的url===
urlpatterns = [
    path("", main_views.index, name="main"),  # http://127.0.0.1:8000/main/
    path('edit/info/', main_views.edit_value, name="main_edit_info"),
    path('change/pwd/', main_views.change_pass, name="main_change_pwd"),
    path('logout/', main_views.user_logout, name="main_logout"),
]