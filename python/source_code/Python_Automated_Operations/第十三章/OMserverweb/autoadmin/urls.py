from django.conf.urls.defaults import *

urlpatterns = patterns('autoadmin.views',
    (r'^$','index'),
    (r'server_fun_categ/$','server_fun_categ'),
    (r'server_app_categ/$','server_app_categ'),
    (r'server_list/$','server_list'),
    (r'module_list/$','module_list'),
    (r'module_info/$','module_info'),
    (r'module_run/$','module_run'),
    (r'module_add/$','module_add'),
    (r'module_add_post/$','module_add_post'),
)
