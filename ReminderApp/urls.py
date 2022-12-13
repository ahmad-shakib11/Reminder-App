"""ReminderApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import Demo.views as Demo_views
import django.contrib.auth.views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Demo_views.HomePage,name='home'),
    path('Create New Reminder/', Demo_views.CreateNewReminder,name='createnewreminder'),
    path('Title/', Demo_views.Title,name='title'),
    path('Date/', Demo_views.Date,name='date'),
    path('Time/', Demo_views.Time,name='time'),
    path('Mark as done/', Demo_views.Markasdone,name='markasdone'),
    path('Settings/', Demo_views.Settings,name='settings'),
    path('register/',Demo_views.register),
    path('login/',auth_views.LoginView.as_view(template_name='login.html')),
    ]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
