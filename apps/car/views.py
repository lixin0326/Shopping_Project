from django.db.models import F
from django.shortcuts import render
from apps.home.models import *


def add(request):
    """
    参数 商品的数量
    参数 商品的id

    当商品已经存在用户的购物车的时候,更新数量
    当商品不存在用户的购物车时候,创建该条记录

    """
    try:
        shop_id = request.GET.get('shop_id')
        number = request.GET.get('number')
        uid = request.user.id
        car = ShopCar.objects.get(uid=uid, shop_id=shop_id, status=1)
        if car:
            car.number = F('number') + number
            # car.number += number
            car.save(update_fields=['number'])
            # ShopCar.objects.select_for_update 高并发
        else:
            car = ShopCar(uid=uid, number=number)
            car.save()
    except:
        pass

    return render(request)


def delete(request):
    return render(request)


def update_num(request):
    return render(request)


def find(request):
    return render(request)
