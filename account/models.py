from django.db import models
from datetime import date
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (
        (u"M", u"Male"),
        (u"F", u"Female"),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT)
    country = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    phone = PhoneNumberField(
        blank=True,
        null=True,
        unique=True
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d',
        blank=True
    )

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def fullname(self):
        return '{} {}'.format(self.user.last_name, self.user.first_name)

    def username(self):
        return self.user.username

    def age(self):
        today = date.today()
        if self.date_of_birth:
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
