import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoginForm, RegistrationForm, UserEditFrom, ProfileEditFrom
from .forms import AdminUserRegistrationForm, AdminUserEditForm
from .models import Profile


# Account views
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
def account_dashboard(request):
    return render(request, 'account_view_dashboard.html')


# Admin views
class AccountAdminUserRegistrationView(CreateView):
    model = User
    template_name = 'admin_user_registration.html'
    form_class = AdminUserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(AccountAdminUserRegistrationView, self).get_context_data(**kwargs)
        context["title"] = "User registration"
        return context

    def form_valid(self, form):
        usr = form.save()
        profile = Profile.objects.create(user=usr)
        usr.date_joined = datetime.datetime.now()
        usr.is_active = form.cleaned_data['is_active']
        usr.is_staff = form.cleaned_data['is_staff']
        usr.is_superuser = form.cleaned_data['is_superuser']
        messages.success(self.request, 'User {} {} has been successfully added.'.format(usr.first_name, usr.last_name))
        return super(AccountAdminUserRegistrationView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('club')
        if self.request.POST.get('_addanother'):
            return reverse_lazy('account:admin_user_registration')
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:admin_profile_edit', kwargs={'pk': self.object.pk})


class AccountAdminUserEditView(UpdateView):
    model = User
    template_name = 'admin_user_edit.html'
    form_class = AdminUserEditForm

    @property
    def has_permission(self):
        return self.user.is_active and self.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(AccountAdminUserEditView, self).get_context_data(**kwargs)
        context["title"] = "User info update"
        return context

    def form_valid(self, form):
        usr = form.save()
        messages.success(self.request, 'User {} {} has been successfully updated.'.format(usr.first_name, usr.last_name))
        return super(AccountAdminUserEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:admin_user_edit', kwargs={'pk': self.object.pk})
