from datetime import datetime
from django.db import models
from django.urls import reverse

from events.models import EventAbstract
from django.contrib.auth.models import User


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self):
        events = Event.objects.filter(is_active=True, is_deleted=False)
        return events

    '''def get_active_events(self):
        active_events = Event.objects.filter(is_active=True, is_deleted=False)
        return active_events

    def get_user_events(self, user):
        user_events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return user_events

    def get_actual_events(self):
        actual_events = Event.objects.filter(is_active=True, is_deleted=False, subscribe_date__gte=datetime.now().date()).order_by("subscribe_date")
        return actual_events'''


class Event(EventAbstract):
    """ Event model """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    subscribe_date = models.DateField()

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("events:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'



