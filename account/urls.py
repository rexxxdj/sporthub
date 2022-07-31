from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.edit_account, name='edit_account'),
    path('profile/', views.edit_profile, name='edit_profile'),
]
