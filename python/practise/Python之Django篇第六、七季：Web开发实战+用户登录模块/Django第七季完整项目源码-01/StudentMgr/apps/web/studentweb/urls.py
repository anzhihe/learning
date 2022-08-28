from django.urls import path
# 引入views
from web.studentweb.views import student as student_views
from web.studentweb.views import student_image as student_image_views

# ==== 匹配当前app中的url===
urlpatterns = [

    # =========== 学生信息 /student/info/ ===========
    path('info/', student_views.index, name="student"),  # 匹配：http://127.0.0.1:8000/student/info/
    path('info/list/', student_views.list_values, name="list_student"),
    path('info/sno/exists/', student_views.is_sno_exists, name="is_sno_exists"),
    path('info/add/', student_views.add_value, name="add_student"),
    path('info/edit/', student_views.edit_value, name="edit_student"),
    path('info/del/', student_views.del_value, name="del_student"),

    # =========== 学生信息 /student/image/ ===========
    path('image/', student_image_views.index, name="student_image"),
    path('image/upload/', student_image_views.upload, name="student_image_upload"),
    path('image/list/', student_image_views.list_value, name="list_student_image"),
    path('image/edit/', student_image_views.edit_value, name="edit_student_image"),
    path('image/del/', student_image_views.del_value, name="del_student_image"),
]
