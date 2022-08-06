from django.urls import path
from . import views


app_name = "events"
urlpatterns = [
    path('', views.EventListView.as_view(), name='list'),
    path('add/', views.EventCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete'),
]
