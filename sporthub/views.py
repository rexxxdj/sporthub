from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from events.models import Event


def index(request):
    return redirect('account/signin')


def forgot_password(request):
    return render(request, 'forgot-password.html', {})


def settings(request):
    return render(request, 'settings.html', {})


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "calendarapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.get_all_events(user=request.user)
        running_events = Event.objects.get_running_events(user=request.user)
        latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
        }
        return render(request, self.template_name, context)
