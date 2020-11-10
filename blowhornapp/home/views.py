from django.shortcuts import render
from django.urls import reverse
# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):

    return render(request, 'home.html', {'data': []})
    # if request.user.is_authenticated:
    #     return render(request, 'hrm/home.html')
    # else:
    #     return render(request, 'hrm/login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        print("andar aaya......")
        username = request.POST.get('email-id')
        print("username is.....", username)

        password = request.POST.get('password')
        print("Password is........", password)
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        print("andar nahin aaya.....")
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        print("coming....")
        username = request.POST.get('name')
        print("signup username.....", username)
        password = request.POST.get('password1')
        print("password......", password)

        try:
            User.objects.create_user(username=username,  password=password, is_staff=True)
        except Exception as e:
            print(e)
            return HttpResponse("User creation data is wrong.")
        return HttpResponseRedirect(reverse('index'))
    else:
        print("coming here naa.....")
        return render(request, 'index.html')