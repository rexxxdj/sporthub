from django.urls import path
from .views import user_login, user_registration, user_logout, account
from .views import edit_profile, edit_user, account_dashboard
from .views import AccountAdminUserRegistrationView, AccountAdminUserEditView, AccountAdminProfileEditView



app_name = 'account'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', account, name='account'),
    path('profile_edit/', edit_profile, name='edit_profile'),
    path('user_edit/', edit_user, name='edit_user'),
    path('dashboard/', account_dashboard, name='dashboard'),
    path('admin/user_add/', AccountAdminUserRegistrationView.as_view(), name='admin_user_registration'),
    path('admin/user_edit/<int:pk>/', AccountAdminUserEditView.as_view(), name='admin_user_edit'),
    path('admin/profile_edit/<int:pk>/', AccountAdminProfileEditView.as_view(), name='admin_profile_edit'),
    #path('admin/profile_edit/', views.account_admin_edit_profile, name='admin_edit_profile'),
]
