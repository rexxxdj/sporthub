# Generated by Django 4.0.6 on 2022-08-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileType',
            field=models.ManyToManyField(to='account.profiletype'),
        ),
    ]
