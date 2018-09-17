from django.http import HttpResponse
from django.shortcuts import render
from apps.home.models import *


def index(request):
    # 获取导航菜单的数据
    navigation = Navigation.objects.all()
    # 分类菜单的数据
    # 三个表
    categories = Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.subs2 = sub.submenu2_set.all()
    # 轮播图数据
    banner = Banner.objects.all()

    return render(request, 'index.html', {'navigation': navigation, 'banner': banner, 'categories': categories})
