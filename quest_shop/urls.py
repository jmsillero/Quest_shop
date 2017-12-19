"""test_project URL Configuration

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
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from shop_app.api.views.Category import CategoryViewSet
from shop_app.api.views.Promotion import PromotionViewSet
from shop_app.api.views.Shop import ShopViewSet
from shop_app.api.views.User import UserViewSet

from quest_shop import settings
from shop_app.api.views.Product import *
from shop_app.shop_site.views.user import site_login, site_register, site_logout
from shop_app.shop_site.views  import dashboard
from shop_app.shop_site.views.shop import create, index, show_shop
from shop_app.shop_site.views import product

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'promotion', PromotionViewSet)
router.register(r'user', UserViewSet)
router.register(r'shop', ShopViewSet)


api_url = [
    url(r'^product/category/(?P<categoryId>[^/.]+)/$', products_by_category, name='product-by-category'),
    url(r'^product/(?P<productId>[^/.]+)/relastets/$', relastets_product, name='relastets-products'),
    url(r'^', include(router.urls)),
]


admin_site_url = [
    url(r'^login/$', site_login, name="login"),
    url(r'^register/$', site_register, name='register'),
    url(r'^logout/$', site_logout, name='logout'),

#shops
    url(r'^$', dashboard.index, name='index'),
    url(r'^shop/list/$', index, name='admin-shop-list'),
    url(r'^shop/create/$', create, name='shop-create'),
    url(r'^shop/details/(?P<shopId>[^/.]+)/$', show_shop, name='show-shop'),

#products
    url(r'product/list/(?P<shopId>[^/.]+)/$', product.index, name='admin-product-list'),
    url(r'^product/create/(?P<shopId>[^/.]+)/$', product.create, name='product-create'),
]



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^myshop/', include(admin_site_url)),


    #api
    url(r'^api/v1/', include(api_url)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
