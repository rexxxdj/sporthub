from django.views.generic.list import ListView
from ..models import Profile


class ProfileListView(ListView):
    model = Profile
    template_name = "other/profile_list.html"
    ordering = ['user__last_name', 'user__first_name']
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().exclude(profileType=4) #exclude Couch

    def get_context_data(self):
        context = super(ProfileListView, self).get_context_data()
        return context
