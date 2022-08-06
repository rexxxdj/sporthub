import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..forms import SignUpForm, SignInForm, UserUpdateForm, ProfileUpdateForm
from ..models import Profile


class SignUpView(CreateView):
    model = User
    template_name = 'registrations/signup.html'
    form_class = SignUpForm

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        new_user = form.save()
        new_user.set_password(form.cleaned_data['password'])
        profile = Profile.objects.create(user=new_user)
        new_user.date_joined = datetime.datetime.now()
        new_user.is_active = True
        login(self.request, new_user)
        messages.success(self.request, 'User {} {} has been successfully added.'.format(form.cleaned_data['first_name'], form.cleaned_data['last_name']))
        return super(SignUpView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:profile_update', kwargs={'pk': self.object.profile.pk})


def user_login(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
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
        form = SignInForm()
    return render(request, 'registrations/signin.html', {'form': form})


class UserUpdateView(UpdateView):
    model = User
    template_name = 'account/update.html'
    form_class = UserUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'User {} {} has been successfully updated.'.format(user.first_name, user.last_name))
        return super(UserUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('account:update', kwargs={'pk': self.object.pk})
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:profile_update', kwargs={'pk': self.object.profile.pk})


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'account/profile_update.html'
    form_class = ProfileUpdateForm

    @property
    def has_permission(self):
        return self.user.is_active

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        profile = form.save()
        messages.success(self.request, 'Profile has been successfully updated.')
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        if self.request.POST.get('_save'):
            return reverse_lazy('account:profile_update', kwargs={'pk': self.object.pk})
        if self.request.POST.get('_continue'):
            return reverse_lazy('account:update', kwargs={'pk': self.object.user.pk})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/account/signin')


@login_required
def account(request):
    return redirect('update/')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')
