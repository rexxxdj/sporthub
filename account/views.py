from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from .forms import LoginForm, RegistrationForm, UserEditFrom, ProfileEditFrom, AdminUserRegistrationForm
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
                    return redirect('/account/dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'auth_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/login')


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
            return HttpResponseRedirect("/account")
    else:
        form = RegistrationForm()
    return render(request, 'auth_register.html', {'form': form})


@login_required
def account_dashboard(request):
    return render(request, 'account_view_dashboard.html')


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
                          'account_edit_profile.html',
                          {'profile_form': profile_form})
        else:
            messages.error(request, 'Error updating your profile')
            return render(request,
                          'account_edit_profile.html',
                          {'profile_form': profile_form})
    else:
        profile_form = ProfileEditFrom(instance=request.user.profile)
        return render(request,
                      'account_edit_profile.html',
                      {'profile_form': profile_form})


@login_required
def account(request):
    return redirect('user_edit/')


@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserEditFrom(
            instance=request.user,
            data=request.POST
        )
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User updated successfully')
            return render(request,
                          'account_edit_user.html',
                          {'user_form': user_form})
        else:
            messages.error(request, 'Error updating your profile')
            return render(request,
                          'account_edit_user.html',
                          {'user_form': user_form})
    else:
        user_form = UserEditFrom(instance=request.user)
        return render(request,
                      'account_edit_user.html',
                      {'user_form': user_form})


def account_admin_user_registration(request):
    user_status = (
        {'id': 1, 'name': 'Active'},
        {'id': 2, 'name': 'Staff Status'},
        {'id': 3, 'name': 'Superuser Status'},
    )
    if request.method == 'POST':
        form = AdminUserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            ''' check User Permission Group
                1 - Administrator
                2 - Moderator
                3 - Couch
                4 - Root
            '''
            try:
                if request.POST['Administrator']:
                    group = Group.objects.get(name='Administrator')
                    new_user.groups.add(group)
            except Exception:
                pass
            try:
                if request.POST['Moderator']:
                    group = Group.objects.get(name='Moderator')
                    new_user.groups.add(group)
            except Exception:
                pass
            try:
                if request.POST['Couch']:
                    group = Group.objects.get(name='Couch')
                    new_user.groups.add(group)
            except Exception:
                pass
            try:
                if request.POST['Root']:
                    group = Group.objects.get(name='Root')
                    new_user.groups.add(group)
            except Exception:
                pass
            ''' check user status'''
            try:
                if request.POST['Active']:
                    new_user.is_active = True
            except Exception:
                pass
            try:
                if request.POST['Staff Status']:
                    new_user.is_staff = True
            except Exception:
                pass
            try:
                if request.POST['Superuser Status']:
                    new_user.is_superuser = True
            except Exception:
                pass
            profile = Profile.objects.create(user=new_user)
            messages.success(request, 'New user was created')
            print(new_user.id)
            return HttpResponseRedirect("/account/admin/user_edit/{}/".format(new_user.id))
    else:
        form = AdminUserRegistrationForm()
    return render(request, 'admin_user_registration.html',
                  {'permission_groups': Group.objects.all().order_by('name'),
                   'user_status': user_status,
                   'form': form})


'''
def account_admin_add_user(request):
    if request.method == "POST":
        if request.POST.get('submit') is not None:
            #TODO validate input
            errors = {}
            if not errors:
                user = User(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    password=request.POST['password'],
                    password2=request.POST['password2'],

                )
    return render(request, 'admin_user_registration.html',
                  {'permission_groups': Group.objects.all().order_by('name'),
                   'form': form})
'''
'''
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
            messages.success(request, 'New user was created')
            return HttpResponseRedirect("/account/admin/user_edit")
    else:
        form = RegistrationForm()
    return render(request, 'admin_user_registration.html', {'form' : form})
'''


def account_admin_edit_user(request):
    if request.method == 'POST':
        user_form = UserEditFrom(
            instance=request.user,
            data=request.POST
        )
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User updated successfully')
            return render(request,
                          'account_edit_user.html',
                          {'user_form': user_form})
        else:
            messages.error(request, 'Error updating your profile')
            return render(request,
                          'account_edit_user.html',
                          {'user_form': user_form})
    else:
        user_form = UserEditFrom(instance=request.user)
        return render(request,
                      'account_edit_user.html',
                      {'user_form': user_form})
