from django.urls import path
from .views import user_login, user_logout, account
from .views import account_dashboard, ProfileListView
from .views import AccountUserRegistrationView, AccountUserEditView, AccountProfileEditView
from .views import AccountAdminUserRegistrationView, AccountAdminUserEditView, AccountAdminProfileEditView



app_name = 'account'
urlpatterns = [
    path('registration/', AccountUserRegistrationView.as_view(), name='account_user_registration'),
    path('login/', user_login, name='account_user_login'),
    path('logout/', user_logout, name='logout'),
    path('', account, name='account'),

    path('user/<int:pk>/edit/', AccountUserEditView.as_view(), name='account_user_edit'),
    path('profile/<int:pk>/edit/', AccountProfileEditView.as_view(), name='account_profile_edit'),

    path('dashboard/', account_dashboard, name='account_dashboard'),
    path('profile_list/', ProfileListView.as_view(), name='profile_list'),

    path('admin/user_add/', AccountAdminUserRegistrationView.as_view(), name='admin_user_registration'),
    path('admin/user_edit/<int:pk>/', AccountAdminUserEditView.as_view(), name='admin_user_edit'),
    path('admin/profile_edit/<int:pk>/', AccountAdminProfileEditView.as_view(), name='admin_profile_edit'),
    #path('admin/profile_edit/', views.account_admin_edit_profile, name='admin_edit_profile'),
]
