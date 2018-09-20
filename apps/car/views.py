from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect

from account.context_processors import shop_count
from apps.home.models import *
from django.http import HttpResponse, JsonResponse


@login_required
def add(request):
    """
    参数 商品的数量
    参数 商品的id

    当商品已经存在用户的购物车的时候,更新数量
    当商品不存在用户的购物车时候,创建该条记录

    """
    # 　
    if request.is_ajax():
        if request.uesr.is_authenticated:
            try:
                shop_id = request.GET.get('shop_id')
                number = request.GET.get('number')
                uid = request.user.userprofile.uid
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
                data = shop_count(request)
                status = 200
                msg = 'success'
                return JsonResponse(data=data)
            except Exception as e:
                return JsonResponse(data={'status': 404, 'msg': 'error'})
        else:
            # 表示没有登录
            return redirect('/account/login/?next=%s' % request.path)
    else:
        # 表示不是ajax请求
        return HttpResponse('不是ajax请求!')


def delete(request):
    pass


def update_num(request):
    pass


def list_result(request):
    # cars = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1)
    # for car in cars:
    #     car.shop.img = car.shop.shopimage_set.all().first()
    return render(request, 'cart.html')
