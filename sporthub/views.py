from django.shortcuts import render, redirect


def index(request):
    return redirect('account/login')


def forgot_password(request):
    return render(request, 'auth_forgot-password.html', {})


def settings(request):
    return render(request, 'settings.html', {})
