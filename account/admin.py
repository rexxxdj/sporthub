from django.contrib import admin
from .models import Profile, ProfileType


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date_of_birth', 'photo', 'degree']
    list_display_links = ['user']
    list_editable = ['date_of_birth', 'degree']
    ordering = ['id', 'user', 'date_of_birth', 'degree']
    list_filter = ['profileType__typeName', 'degree']
    list_per_page = 10
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'profileType__typeName']


class ProfileTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'typeName']
    list_display_links = ['id', 'typeName']
    ordering = ['id', 'typeName']
    list_per_page = 10
    search_fields = ['typeName']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileType, ProfileTypeAdmin)
