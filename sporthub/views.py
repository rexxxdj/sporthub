from django.shortcuts import render, redirect


def index(request):
    return redirect('/login')


def forgot_password(request):
    return render(request, 'forgot-password.html', {})


def settings(request):
    return render(request, 'settings.html', {})
