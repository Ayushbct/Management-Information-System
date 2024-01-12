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


    path('course', views.course,name='course'),
    path('course_delete/<int:id>', views.course_delete,name='course_delete'),
    path('course_update/<int:id>', views.update_course, name='course_update'),

    path('subject', views.subject,name='subject'),
    path('subject_delete/<int:id>', views.subject_delete,name='subject_delete'),
    path('subject_update/<int:id>', views.update_subject, name='subject_update'),


    path('subjectstudent', views.subjectstudent,name='subjectstudent'),
    path('subjectstudent_delete/<int:id>', views.subjectstudent_delete,name='subjectstudent_delete'),
    path('subjectstudent_update/<int:id>', views.update_subjectstudent, name='subjectstudent_update'),

    path('attendance', views.attendance,name='attendance'),
    path('attendance_delete/<int:id>', views.attendance_delete,name='attendance_delete'),
    path('attendance_update/<int:id>', views.update_attendance, name='attendance_update'),

    path('student', views.student,name='student'),
    path('student_delete/<int:id>', views.student_delete,name='student_delete'),
    path('student_update/<int:id>', views.update_student, name='student_update'),


    path('routine', views.routine,name='routine'),
    path('routine_delete/<int:id>', views.routine_delete,name='routine_delete'),
    path('routine_update/<int:id>', views.update_routine, name='routine_update'),


]
