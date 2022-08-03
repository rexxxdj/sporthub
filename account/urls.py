from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.account, name='account'),
    path('profile_edit/', views.edit_profile, name='edit_profile'),
    path('user_edit/', views.edit_user, name='edit_user'),
    path('dashboard/', views.account_dashboard, name='dashboard'),
    path('admin/user_add/', views.account_admin_user_registration, name='admin_user_registration'),
    path('admin/user_edit/', views.account_admin_edit_user, name='admin_edit_user'),
    #path('admin/profile_edit/', views.account_admin_edit_profile, name='admin_edit_profile'),
]
