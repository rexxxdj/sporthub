from django.urls import path
from . import views


app_name = "events"
urlpatterns = [
    path('list/', views.EventListView.as_view(), name='list'),
    path('calendar/', views.EventCalendarView.as_view(), name='calendar'),
    path('add/', views.EventCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete'),
]
