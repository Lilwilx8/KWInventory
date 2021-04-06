from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm



def login(request):
    return render(request, "login.html")


def logout(request):
    do_logout(request)
    return redirect('Login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('Login')

    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, "register.html", context)


def Home(request):
    return render(request, 'home.html')


def User(request):
    return render(request, 'user.html')



