from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.shortcuts import render
from apps.home.models import ShopCar
from django.http import HttpResponse


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
        else:
            return HttpResponse("不存在该用户!或该用户未激活!")


def register_view(request):


    return render(request, 'register.html')
