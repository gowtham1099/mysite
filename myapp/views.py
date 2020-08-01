from django.shortcuts import render, redirect
from .forms import Usercreation, RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth


# Create your views here.

def register(request):
    form = Usercreation()
    if request.method == 'POST':
        form = Usercreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created Succssfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request, "Invalid username/password")

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def main(request):
    f = RegistrationForm()
    if request.method == 'POST':
        f = RegistrationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Submitted Successfully')
        return redirect('main')
    con = {'f': f}
    return render(request, 'main.html', con)
