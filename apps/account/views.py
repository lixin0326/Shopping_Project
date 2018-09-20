from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect
from apps.home.models import *
from django.http import HttpResponse, JsonResponse


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            user.count = ShopCar.objects.filter(user_id=user.userprofile.uid).aggregate(
                sum=Sum('number')).get('sum')  # 聚合函数
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("不存在该用户!或该用户未激活!")


# 登出操作
def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        user = User.objects.filter(username=username)
        if user:
            return JsonResponse(request, 'register.html', {'msg': '该用户已经存在!'})
        else:
            # 先保存主表的数据,然后在把主表的id给子表的外键字段(一对一映射关系)
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            UserProfile.objects.create(user_id=user.id, phone=phone)
            user.save()
        return redirect('/')
