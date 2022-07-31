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
        return super().get_queryset().exclude(profileType=3) #exclude Couch

    def get_context_data(self):
        context = super(ProfileListView, self).get_context_data()
        #context["profilecnt"] = Profile.objects.all().count()
        return context

    #def get_queryset(self):
    #   profile_id = self.request.GET.get('profile_id', 'None')
    #    if profile_id:
    #        profile_list = Profile.objects.filter()


#def club_list(request):
#    profiles = Profile.objects.all()
#    return render(request, 'all_view_profile_list.html', {'profiles': profiles})
