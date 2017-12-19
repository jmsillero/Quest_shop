from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import  render, redirect
from django.views.decorators.csrf import csrf_protect

from shop_app.models import Profile
from shop_app.shop_site.forms.user import LoginForm, RegisterForm





@csrf_protect
def site_login(request):
    message = None
    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            try:
                email = User.objects.get(email=email).email
                user = authenticate(username=email, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('index')
                    else:
                        message = 'Your user is inactive'
                else:
                    message = 'Invalid email or password'
            except Exception:
                message = 'Invalid email or password'
    else:
        form_login = LoginForm()

    return render(request, 'user/login.html', {'message': message, 'form_login': form_login})


@csrf_protect
def site_register(request):
    message = None
    if request.method == 'POST':
        form_register = RegisterForm(request.POST)
        if form_register.is_valid():
            email = request.POST['email']
            last_name = request.POST['last_name']
            address = request.POST['address']
            password = request.POST['password1']
            name = request.POST['name']

            if User.objects.filter(email=email):
                message = 'User is already in the system.'
            else:
                user = User.objects.create_user(email, email, password)
                user.first_name = name
                user.last_name = last_name
                user.is_active = True
                user.save()

                profile = Profile.objects.create(user = user, address = address, type="Owner")
                profile.save()

                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect('index')

    else:
        form_register = RegisterForm()
    a = form_register.errors

    return render(request, 'user/register.html', {'message': message, 'form_register': form_register})

@login_required(login_url='/myshop/login/')
def site_logout(request):
    logout(request)
    return redirect('login')



