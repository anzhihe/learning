from django.urls import path
# 引入views
from studentweb.views import student as student_views

# ==== 匹配当前app中的url===
urlpatterns = [
    path('', student_views.index, name="student"),  # 匹配：http://127.0.0.1:8000/student/
    path('list/', student_views.list_values, name="list_student"),
    path('sno/exists/', student_views.is_sno_exists, name="is_sno_exists"),
    path('add/', student_views.add_value, name="add_student"),
    path('edit/', student_views.edit_value, name="edit_student"),
    path('del/', student_views.del_value, name="del_student"),
]
