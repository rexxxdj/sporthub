from django.db import models
from datetime import date
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class ProfileType(models.Model):
    typeName = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        verbose_name='Profile Type'
    )

    def __str__(self):
        return self.typeName


class Profile(models.Model):
    GENDER_CHOICES = (
        (u"M", u"Male"),
        (u"F", u"Female"),
    )
    DEGREE_CHOICES = (
        (u"Mukyu", u"White belt "),
        (u"10th Kyu", u"10 Kyu - Orange belt"),
        (u"9th Kyu", u"9th Kyu – Orange belt with blue stripe"),
        (u"8th Kyu", u"8th Kyu - Blue belt"),
        (u"7th Kyu", u"7th Kyu – Blue belt with green stripe"),
        (u"6th Kyu", u"6th Kyu – Yellow belt"),
        (u"5th Kyu", u"5th Kyu – Yellow belt with orange stripe"),
        (u"4th Kyu", u"4th Kyu – Green belt"),
        (u"3rd Kyu", u"3rd Kyu – Green belt with brown stripe"),
        (u"2nd Kyu", u"2nd Kyu – Brown belt"),
        (u"1st Kyu", u"1st Kyu – Brown belt with black stripe"),
        (u"1st Dan (Shodan)", u"1st Dan - The black belt has one gold stripe"),
        (u"1st Dan (Nidan)", u"2nd Dan – The black belt has two gold stripes"),
        (u"1st Dan (Sandan)", u"3rd Dan – The black belt has three gold stripes"),
        (u"1st Dan (Yondan)", u"4th Dan – The black belt has four gold stripes"),
        (u"1st Dan (Godan)", u"5th Dan - The black belt has five gold stripes"),
        (u"1st Dan (Rokudan)", u"6th Dan – The black belt has six gold stripes"),
        (u"1st Dan (Shichidan)", u"7th Dan – The black belt has seven gold stripes"),
        (u"1st Dan (Hachidan)", u"8th Dan – The black belt has eight gold stripes"),
        (u"1st Dan (Kyūdan)", u"9th Dan – The black belt has nine gold stripes"),
        (u"1st Dan (Jūdan)", u"10th Dan – The black belt has ten gold stripes")
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
    degree = models.CharField(
        max_length=20,
        choices=DEGREE_CHOICES,
        blank=True,
        null=True
    )
    profileType = models.ForeignKey(
        ProfileType,
        null=True,
        blank=True,
        on_delete=models.PROTECT
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
