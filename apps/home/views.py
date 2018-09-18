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
        # 分类菜单数据
        category.subs = category.submenu_set.all()
        for sub in category.subs:
            sub.subs2 = sub.submenu2_set.all()

        category.shops = category.shop_set.values('shop_id', 'name', 'promote_price')
        for shop in category.shops:
            shop.update(img=ShopImage.objects.filter(shop_id=shop.get('shop_id')).first())

    # 轮播图数据
    banner = Banner.objects.all()

    return render(request, 'index.html', {'navigation': navigation,
                                          'banner': banner,
                                          'categories': categories,
                                          })
