from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import (UserRegistrationView,getUserHome,
UserLoginView,UserProfileView,UserChangePassword,
SendPasswordResetEmailView,UserPasswordResetView,getUsers,getTeacher)


urlpatterns=[
    path('',getUserHome,name='user_home'),
    path('getuser/',getUsers,name="get_user"),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/',UserProfileView.as_view(),name="profile"),
    path('changepassword/',UserChangePassword.as_view(),name="change_password"),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name="send_reset_password_email"),
    path('reset/<uid>/<token>/',UserPasswordResetView.as_view(),name="send"),
    path('getteacher/<tid>',getTeacher,name="get_teacher"),
]