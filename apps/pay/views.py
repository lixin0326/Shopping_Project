from django.shortcuts import render
# from alipay import AliPay
from django.views.decorators.csrf import csrf_exempt

from First_Project import settings


# def pay(request):
#     alipay = AliPay(
#         appid=settings.APP_ID,
#         app_notify_url='http://127.0.0.1:8080/pay/callback/',
#         # app_private_key_string=settings.APP_PRIVATE_STRING,
#         # alipay_public_key_string=settings.APP_PUBLIC_STRING,
#         debug=True,
#     )
#     order_url = alipay.api_alipay_trade_page_pay(
#         subject='测试支付123456',
#         out_trade_no='666',
#         total_amount='1.00',
#         # 支付成功后 前端跳转的页面 get请求
#         return_url='http://www.baidu.com'
#
#     )


@csrf_exempt
def notify_callback(request):
    pass
