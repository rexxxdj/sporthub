from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, UserEditFrom, ProfileEditFrom
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            messages.success(request, 'New user was created')
            return HttpResponseRedirect("/profile")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})


@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileEditFrom(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return render(request,
                          'profile.html',
                          {'profile_form': profile_form})
        else:
            messages.error(request, 'Error updating your profile')
            return render(request,
                          'profile.html',
                          {'profile_form': profile_form})
    else:
        profile_form = ProfileEditFrom(instance=request.user.profile)
        return render(request,
                      'profile.html',
                      {'profile_form': profile_form})


@login_required
def edit_account(request):
    if request.method == 'POST':
        user_form = UserEditFrom(
            instance=request.user,
            data=request.POST
        )
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User updated successfully')
            return render(request,
                          'account.html',
                          {'user_form': user_form})
        else:
            messages.error(request, 'Error updating your profile')
            return render(request,
                          'account.html',
                          {'user_form': user_form})
    else:
        user_form = UserEditFrom(instance=request.user)
        return render(request,
                      'account.html',
                      {'user_form': user_form})


