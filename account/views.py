import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoginForm, AccountUserRegistrationForm, AccountUserEditForm, AccountProfileEditFrom
from .forms import AdminUserRegistrationForm, AdminUserEditForm, AdminProfileEditForm
from .models import Profile


# Account views
class AccountUserRegistrationView(CreateView):
    model = User
    template_name = 'auth_registration.html'
    form_class = AccountUserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super(AccountUserRegistrationView, self).get_context_data(**kwargs)
        context["title"] = "User registration"
        return context

    def form_valid(self, form):
        new_user = form.save()
        new_user.set_password(form.cleaned_data['password'])
        profile = Profile.objects.create(user=new_user)
        new_user.date_joined = datetime.datetime.now()
        new_user.is_active = True
        login(self.request, new_user)
        messages.success(self.request, 'User {} {} has been successfully added.'.format(form.cleaned_data['first_name'], form.cleaned_data['last_name']))
        return super(AccountUserRegistrationView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:account_profile_edit')


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


class AccountUserEditView(UpdateView):
    model = User
    template_name = 'account_user_edit.html'
    form_class = AccountUserEditForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(AccountUserEditView, self).get_context_data(**kwargs)
        context["title"] = "User info update"
        return context

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User {} {} has been successfully updated.'.format(user.first_name, user.last_name))
        return super(AccountUserEditView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('account:account_user_edit', kwargs={'pk': self.object.pk})
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:account_profile_edit', kwargs={'pk': self.object.profile.pk})


class AccountProfileEditView(UpdateView):
    model = Profile
    template_name = 'account_profile_edit.html'
    form_class = AccountProfileEditFrom

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(AccountProfileEditView, self).get_context_data(**kwargs)
        context["title"] = "User info update"
        return context

    def form_valid(self, form):
        profile = form.save()
        messages.success(self.request, 'Profile has been successfully updated.')
        return super(AccountProfileEditView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('account:account_profile_edit', kwargs={'pk': self.object.pk})
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:account_user_edit', kwargs={'pk': self.object.user.pk})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/login')


@login_required
def account(request):
    return redirect('user_edit/')


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
            return reverse_lazy('account:admin_profile_edit', kwargs={'pk': self.object.profile.pk})


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


class AccountAdminProfileEditView(UpdateView):
    model = Profile
    template_name = 'admin_profile_edit.html'
    form_class = AdminProfileEditForm

    @property
    def has_permission(self):
        return self.user.is_active and self.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(AccountAdminProfileEditView, self).get_context_data(**kwargs)
        context["title"] = "User info update"
        return context

    def form_valid(self, form):
        profile = form.save()
        messages.success(self.request, 'Profile for User {} has been successfully updated.'.format(profile.fullname()))
        return super(AccountAdminProfileEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:admin_profile_edit', kwargs={'pk': self.object.pk})
