from django.contrib import admin
from django.conf.urls import url, include
from apps.home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    # 首页
    url('^$', views.index),
    url('home/', include('apps.home.urls')),
    url('account/', include('apps.account.urls')),
    url('car/', include('apps.car.urls')),
    url('cate_detail/', include('apps.cate_detail.urls')),
    url('order/', include('apps.order.urls')),
    url('pay/', include('apps.pay.urls')),
    url('shop_detail/', include('apps.shop_detail.urls')),
]
