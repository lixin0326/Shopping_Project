from django.conf.urls import url

from pay import views

urlpatterns = [
    url('callback/', views.notify_callback),
    # url('alipay/', views.pay),
]
