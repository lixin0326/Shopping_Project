from django.shortcuts import render
from apps.home.models import Shop


def detail(request):
    if request.method == 'GET':
        try:
            ship_id = request.GET.get('id')
            if ship_id:
                # 获取单条的所有信息
                # 用get的时候要小心,要用try来捕获异常一下
                shop = Shop.objects.get(shop_id=ship_id)
                shop.imgs = shop.shopimage_set.all()
                # 获取商品的参数信息
                values = shop.propertyvalue_set.all()

                # 获取商品的评论信息
                reviews = shop.review_set.all()
                # 获取评论数量
                count = shop.review_set.count()

                return render(request, 'detail.html', {'shop': shop,
                                                       'values': values,
                                                       'reviews': reviews,
                                                       'count': count})
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')
