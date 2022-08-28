from django.urls import path
# 引入当前app的views
from mainweb import views as main_views
# ==== 匹配当前app中的url===
urlpatterns = [
    path("", main_views.index, name="main"),  # http://127.0.0.1:8000/main/
]