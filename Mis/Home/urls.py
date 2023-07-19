"""
URL configuration for Mis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Home import views
urlpatterns = [
    path('', views.index,name='home'),
    # path('apitest', views.hello_world,name='helloworld'),
    path('department', views.department,name='department'),

    path('department_delete/<int:id>', views.department_delete,name='department_delete'),
    path('department_update/<int:id>', views.update_department, name='department_update'),
    path('department/<int:id>/', views.department_detail, name='department_detail'),



]
