from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.account, name='account'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.user_login, name='signin'),
    path('signout/', views.user_logout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('list/', views.ProfileListView.as_view(), name='list'),

    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile_update'),

    path('staff/user/signup/', views.StaffUserSignUpView.as_view(), name='staff_user_signup'),
    path('staff/user/<int:pk>/update/', views.StaffUserUpdateView.as_view(), name='staff_user_update'),
    path('staff/profile/<int:pk>/update/', views.StaffProfileUpdateView.as_view(), name='staff_profile_update'),
    path('staff/user/<int:pk>/delete/', views.StaffUserDeleteView.as_view(), name='staff_user_delete')
]
