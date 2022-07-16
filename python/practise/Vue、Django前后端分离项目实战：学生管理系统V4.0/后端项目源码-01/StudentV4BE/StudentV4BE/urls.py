"""StudentV4BE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.get_students),  # 获取所有学生信息的接口
    path('students/query/', views.query_students),  # 查询学生信息的接口
    path('sno/check/', views.is_exists_sno), # 校验学号是否存在
    path('student/add/', views.add_student), # 添加学生信息的接口
    path('student/update/', views.update_student),  # 修改学生信息的接口
    path('student/delete/', views.delete_student),  # 删除学生信息的接口
    path('students/delete/', views.delete_students),  # 删除学生信息的接口
    path('upload/', views.upload), # 上传文件的接口
    path('excel/import/', views.import_students_excel), # 导入Excel文件
    path('excel/export/', views.export_student_excel), # 导出Excel文件
  ]
#添加这行--- 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

