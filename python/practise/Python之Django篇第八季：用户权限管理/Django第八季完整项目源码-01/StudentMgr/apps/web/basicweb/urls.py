from django.urls import path
# 引入当前app的views
from web.basicweb.views import faculty
from web.basicweb.views import major

# ==== 匹配当前app中的url===
urlpatterns = [

    # ============ 院系管理 =========
    path('faculty/', faculty.index, name="faculty"),  # 展示前端页面
    path('faculty/list/', faculty.list_values, name="list_faculty"),  # 获取数据
    path('faculty/add/', faculty.add_value, name="add_faculty"),  # 添加
    path('faculty/edit/', faculty.edit_value, name="edit_faculty"),  # 修改
    path('faculty/del/', faculty.del_value, name="del_faculty"),  # 删除

    # ============ 专业管理 =========
    path('major/', major.index, name="major"),  # 展示前端页面
    path('major/list/', major.list_values, name="list_major"), # 获取数据
    path('major/add/', major.add_value, name="add_major"),  # 添加数据
    path('major/edit/', major.edit_value, name="edit_major"),  # 修改数据
    path('major/del/', major.del_value, name="del_major"),  # 修改数据
    path('major/query/', major.query_value, name="query_major"), # 根据院系查专业

]





"""
获取数据： faculty/list/     或者   ^faculty/list/$
添加： faculty/add/         或者  ^faculty/add/$
修改： faculty/edit/        或者  ^facult/edit/(?P<id>\d+)/$
删除：  faculty/del/        或者  ^facult/del/(?P<id>\d+)/&
"""
