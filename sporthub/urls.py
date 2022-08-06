"""sporthub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from _curses_panel import panel

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from . import views
from account import views as accountViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('account/', include('account.urls', namespace='account')),
    path('events/', include('events.urls', namespace='events')),

    path('settings/', views.settings, name='settings'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
