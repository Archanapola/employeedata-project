"""employeedataproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from empapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data',views.generateDate),
    path('fetching_data',views.fetching_data,name='fetching_data'),
    path('mainpage',views.mainpage,name='mainpage'),
    path('hyd_data',views.hyd_data,name='hyd_data'),
    path('bang_data',views.bang_data,name='bang_data'),
    path('chennai_data',views.chennai_data,name='chennai_data'),
    path('pune_data',views.pune_data,name='pune_data'),
    ]
