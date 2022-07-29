from django.shortcuts import render, redirect
from account.models import Profile


def index(request):
    return redirect('/login')


def forgot_password(request):
    return render(request, 'forgot-password.html', {})


def settings(request):
    return render(request, 'settings.html', {})


def club_list(request):
    profiles = Profile.objects.all()
    return render(request, 'club.html', {'profiles': profiles})
