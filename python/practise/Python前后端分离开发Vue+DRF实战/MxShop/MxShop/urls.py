"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset
from goods.views import IndexCategoryViewset
from users.views import SmsCodeViewset, UserViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset


router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")

#配置category的url
router.register(r'categorys', CategoryViewset, base_name="categorys")

router.register(r'codes', SmsCodeViewset, base_name="codes")

router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")

router.register(r'users', UserViewset, base_name="users")

#收藏
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

#留言
router.register(r'messages', LeavingMessageViewset, base_name="messages")

#收货地址
router.register(r'address', AddressViewset, base_name="address")

#购物车url
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

#订单相关url
router.register(r'orders', OrderViewset, base_name="orders")

#轮播图url
router.register(r'banners', BannerViewset, base_name="banners")

#首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")


goods_list = GoodsListViewSet.as_view({
    'get': 'list',
})

from trade.views import AlipayView
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
	
	url('', include('social_django.urls', namespace='social')),
    url(r'^', include(router.urls)),

    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),

    url(r'docs/', include_docs_urls(title="慕学生鲜")),

    #drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),

    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
]


