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
]
