from django.urls import path,include
from api import views

from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'departments',views.DepartmentViewSet)
router.register(r'years',views.YearViewSet)
router.register(r'students',views.StudentViewSet)

router.register(r'teachers',views.TeacherViewSet)
router.register(r'semesters',views.SemesterViewSet)
router.register(r'subjects',views.SubjectViewSet)
router.register(r'courses',views.CourseViewSet)
router.register(r'subjectstudents',views.SubjectStudentViewSet)
router.register(r'attendances',views.AttendanceViewSet)



urlpatterns = [
    
    # path('', views.getRoutes,name='routes'),
    # path('year', views.getYears,name='years'),
    # path('year/<str:pk>', views.getYear,name='year'),
    path('',include(router.urls)),

    path('deletedepartments/',views.Deletedepartments,name='deletedepartments'),
    path('deleteyears/',views.Deleteyears,name='deleteyears'),
    path('deletestudents/',views.Deletestudents,name='deletestudents'),
    path('deleteteachers/',views.Deleteteachers,name='deleteteachers'),
    path('deletesemesters/',views.Deletesemesters,name='deletesemesters'),
    path('deletesubjects/',views.Deletesubjects,name='deletesubjects'),
    path('deletecourses/',views.Deletecourses,name='deletecourses'),
    path('deletesubjectstudents/',views.Deletesubjectstudents,name='deletesubjectstudents'),
    path('deleteattendances/',views.Deleteattendances,name='deleteattendances'),

 
]
