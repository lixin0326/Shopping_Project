from django.db.models import F
from django.shortcuts import render
from apps.home.models import *
from django.http import HttpResponse


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
        uid = 1
        cars = ShopCar.objects.filter(user_id=uid, shop_id=shop_id, status=1)
        if cars:
            car = cars.first()
            car.number = F('number') + number
            # car.number += number
            car.save(update_fields=['number'])
            # ShopCar.objects.select_for_update 高并发
        else:
            car = ShopCar(user_id=uid, shop_id=shop_id, number=number)
            car.save()
    except Exception as e:
        pass

    return HttpResponse('11111')


def delete(request):
    pass


def update_num(request):
    pass


def find(request):
    pass
