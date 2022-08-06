import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..forms import StaffUserSignUpForm, StaffUserUpdateForm, StaffProfileUpdateForm
from ..models import Profile


class StaffUserSignUpView(CreateView):
    model = User
    template_name = 'staff/user_signup.html'
    form_class = StaffUserSignUpForm

    def get_context_data(self, **kwargs):
        context = super(StaffUserSignUpView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        user.date_joined = datetime.datetime.now()
        user.is_active = form.cleaned_data['is_active']
        user.is_staff = form.cleaned_data['is_staff']
        user.is_superuser = form.cleaned_data['is_superuser']
        messages.success(self.request, 'User {} {} has been successfully added.'.format(user.first_name, user.last_name))
        return super(StaffUserSignUpView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('account:list')
        if self.request.POST.get('_addanother'):
            return reverse_lazy('account:staff_user_signup')
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:staff_profile_update', kwargs={'pk': self.object.profile.pk})


class StaffUserUpdateView(UpdateView):
    model = User
    template_name = 'staff/user_update.html'
    form_class = StaffUserUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active and self.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(StaffUserUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        usr = form.save()
        messages.success(self.request, 'User {} {} has been successfully updated.'.format(usr.first_name, usr.last_name))
        return super(StaffUserUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('account:staff_user_update', kwargs={'pk': self.object.pk})
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:staff_profile_update', kwargs={'pk': self.object.profile.pk})


class StaffProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'staff/profile_update.html'
    form_class = StaffProfileUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active and self.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(StaffProfileUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        profile = form.save()
        messages.success(self.request, 'Profile for User {} has been successfully updated.'.format(profile.fullname()))
        return super(StaffProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:staff_profile_update', kwargs={'pk': self.object.pk})


class StaffUserDeleteView(DeleteView):
    model = User
    template_name = 'staff/user_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('account:list')

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('_cancel'):
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(StaffUserDeleteView, self).post(request, *args, **kwargs)
