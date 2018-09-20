from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from account.context_processors import shop_count
from apps.home.models import *
from django.http import HttpResponse, JsonResponse


@login_required
@csrf_exempt
def add(request):
    """
    参数 商品的数量
    参数 商品的id
    当商品已经存在用户的购物车的时候,更新数量
    当商品不存在用户的购物车时候,创建该条记录

   """

    if request.is_ajax():
        if request.uesr.is_authenticated():
            try:
                shop_id = request.POST.get('shop_id')
                number = request.POST.get('number')
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
                data['status'] = 200
                data['msg'] = 'success'
                return JsonResponse(data=data)
            except Exception as e:
                return JsonResponse(data={'status': 404, 'msg': 'error'})
        else:
            # 表示没有登录
            return redirect('/account/login/?next=%s' % request.path)
    else:
        # 表示不是ajax请求
        return HttpResponse('不是ajax请求!')


@csrf_exempt
def delete(request):
    try:
        car_id = request.POST.get('car_id')
        car = ShopCar.objects.get(car_id=car_id, status=1)
        car.status = -1
        car.save(update_fields=['status'])
        return JsonResponse({'status': 200, 'msg': 'success'})
    except:
        return JsonResponse({'status': 404, 'msg': '删除失败!'})


@login_required
def list_result(request):
    cars = ShopCar.objects.filter(user_id=request.user.userprofile.uid, status=1)
    for car in cars:
        car.shop.img = car.shop.shopimage_set.all().first()
    return render(request, 'cart.html', {'cars': cars})


@csrf_exempt
def update_num(request):
    try:
        action = request.POST.get('action')
        car_id = request.POST.get('car_id')
        if action == '1':
            count = ShopCar.objects.filter(car_id=car_id, status=1).update(number=F('number') + 1)
        else:
            count = ShopCar.objects.filter(car_id=car_id, status=1).update(number=F('number') - 1)
        return JsonResponse({'status': 200, 'msg': 'success'})
    except Exception as e:
        pass
