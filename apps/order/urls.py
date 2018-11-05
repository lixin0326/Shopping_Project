from django.conf.urls import url
from apps.order import views

urlpatterns = [
    url('create/', views.order,name='create_order'),
]
