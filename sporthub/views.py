from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, Permission
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from account.models import Profile


def index(request):
    return redirect('account/login')


def forgot_password(request):
    return render(request, 'auth_forgot-password.html', {})


def settings(request):
    return render(request, 'settings.html', {})


class ProfileListView(ListView):
    model = Profile
    template_name = "all_view_profile_list.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().exclude(profileType=4) #exclude Couch

    def get_context_data(self):
        context = super(ProfileListView, self).get_context_data()
        #context["profilecnt"] = Profile.objects.all().count()
        return context
