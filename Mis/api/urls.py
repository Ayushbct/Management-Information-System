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
router.register(r'routines', views.RoutineViewSet)


urlpatterns = [
    
    # path('', views.getRoutes,name='routes'),
    # path('year', views.getYears,name='years'),
    # path('year/<str:pk>', views.getYear,name='year'),
    path('',include(router.urls)),
    # path('routines/create_routine/', views.RoutineViewSet.as_view({'post': 'create_routine'}), name='create-routine'),

    # URL to retrieve all routines
    # path('routines/', views.RoutineViewSet.as_view({'get': 'create_routine','post': 'create_routine'}), name='list-routines'),

    path('teachers/<int:pk>/subjects/', views.TeacherViewSet.as_view({'get': 'subjects'}), name='teacher-subjects'),

    path('teachers/<int:pk>/subjects/<int:subject_id>/', views.SubjectViewSet.as_view({'get': 'subject'}), name='teacher-subject'),
        
    path('teachers/<int:pk>/subjects/<int:subject_id>/students/', views.StudentViewSet.as_view({'get': 'subject_students'}), name='teacher-subject-students'),
    
    path('teachers/<int:pk>/subjects/<int:subject_id>/students/<int:student_id>/', views.StudentViewSet.as_view({'get': 'subject_student'}), name='teacher-subject-student'),

    path('teachers/<int:pk>/subjects/<int:subject_id>/students/<int:student_id>/attendance/', views.AttendanceViewSet.as_view({'get': 'get_student_attendance','post': 'create_student_attendance'}), name='teacher-subject-student-attendance'),

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
