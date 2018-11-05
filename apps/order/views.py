import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render
from apps.home.models import *
from django.db import transaction

"""
拿到所有被选中的购物车记录
1>第一个 选择地址
2>第二个 选择支付方式
3>第三个 配送方式

提交订单
1>生成订单号
2>更新商品的库存量
3>购物车表

涉及到多个表  多个表的查询 使用关联查询

事务(所有操作要么全部成功,要么全部失败) 

原子性:所有操作要么全部成功,要不全部失败(回滚)
一致性:保持数据的完整性
隔离性:可以多个用户同时操作(注意隔离级别)
持久性:所有操作一旦操作成功,不可撤回

"""


def confirm(request):
    # 获取被选中商品信息
    ids = [12, 13, 14]
    cars = ShopCar.objects.filter(car_id_in=ids)
    return render(request, 'confirm.html', {'cars': cars})


# 结算---确认订单--生成订单 主表是订单表
def order(request):
    ids = [12, 13, 14]
    order_code = f'{datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d%H%M%S")}{random.randint(10,99)}'
    # 　对订单表操作--修改商品的库存量--修改购物车表
    # 第一步 生成订单号(支付平台需要,站内唯一) 格式年月日时分秒
    # f ---format
    with transaction.atomic():
        try:
            # 第二步 往订单表增加记录
            order = Order(order_code=order_code,
                          address='河南省信阳市',
                          mobile='15737628530',
                          receiver='雪慧',
                          user_message='今年回俺家过年呀',
                          user_id=3)
            order.save()
            cars = ShopCar.objects.filter(car_id__in=ids)
            # 总金额
            total = 0.00
            for car in cars:
                car.status = 2
                car.order_id = order.pk
                car.save(update_fields=['status', 'order_id'])
                # 商品库存
                if car.shop.stock >= car.number:
                    car.shop.stock -= car.number
                    car.shop.save(update_fields=['stock'])
                    total += car.number * car.shop.promote_price

                else:
                    pass
        except Exception as e:
            return HttpResponse('123')
        return HttpResponse("成功!")
