from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, UserEditFrom, ProfileEditeFrom
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
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
            return render(request, 'dashboard.html', {'user': new_user})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form' : form})


@login_required
def user_dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditFrom(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileEditeFrom(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditFrom(instance=request.user)
        profile_form = ProfileEditeFrom(instance=request.user.profile)
        return render(request,
                      'profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
