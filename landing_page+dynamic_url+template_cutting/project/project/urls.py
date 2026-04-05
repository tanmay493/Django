"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name="landing"),
    path('home/',views.home,name='home'),
    path('dynamic_int/<int:x>/',views.dynamic_int,name="dynamic_int"),
    path('dynamic_str/<str:x>/',views.dynamic_str,name="dynamic_str"),
    path('dynamic_slug/<slug:x>/',views.dynamic_slug,name="dynamic_slug"),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('feature/',views.feature,name='feature'),
    path('reg_data/',views.reg_data,name='reg_data')

]
