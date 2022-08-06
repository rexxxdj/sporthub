import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoginForm, AccountUserRegistrationForm, AccountUserEditForm, AccountProfileEditFrom
from .forms import AdminUserRegistrationForm, AdminUserEditForm, AdminProfileEditForm
from .models import Profile


# Account views


# Admin views
class AccountAdminUserRegistrationView(CreateView):
    model = User
    template_name = 'user_signup.html'
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
            return reverse_lazy('account:profile_list')
        if self.request.POST.get('_addanother'):
            return reverse_lazy('account:admin_user_registration')
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:admin_profile_edit', kwargs={'pk': self.object.profile.pk})


class AccountAdminUserEditView(UpdateView):
    model = User
    template_name = 'user_update.html'
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
        if self.request.POST.get('_save'):
            return reverse_lazy('account:admin_user_edit', kwargs={'pk': self.object.pk})
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:admin_profile_edit', kwargs={'pk': self.object.profile.pk})


class AccountAdminProfileEditView(UpdateView):
    model = Profile
    template_name = 'profile_update.html'
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


class AccountAdminUserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('account:profile_list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(AccountAdminUserDeleteView, self).post(request, *args, **kwargs)



# All views

