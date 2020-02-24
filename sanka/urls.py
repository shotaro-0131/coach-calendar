"""sanka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from app import views
from django.conf.urls import include, url
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    path('', include('user_sessions.urls', 'user_sessions')),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('plan/', views.Planing.as_view(), name='plan'),
    path('admin/', admin.site.urls),
    # url(r'^myapp/(?P<mode_name>\w+)/$', TemplateView.as_view(template_name='month.html'),
    #     name='myapp-index'),
    path('index/', views.index, name='index'),
    path('month/', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    # path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name="/login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page="polls:index"), name='logout'),
]
