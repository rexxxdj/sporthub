
from django.db import models

from django.contrib.auth.models import User
from events.models import Event, EventAbstract


'''class EventMember(EventAbstract):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_members"
    )
    weight = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
'''
