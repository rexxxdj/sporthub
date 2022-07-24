# Generated by Django 4.0.6 on 2022-07-23 18:14

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_address_profile_city_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]