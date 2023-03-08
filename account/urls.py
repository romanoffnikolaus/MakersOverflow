from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

from . import views

urlpatterns = [
    path(
        'register/',
        views.RegistrationView.as_view()),
    path(
        'activate/<str:email>/<str:activation_code>/',
        views.ActivationView.as_view(),
        name='activate'),
    path(
        'login/',
        views.LoginView.as_view(),
        name='token_obtain_pair'),
    path(
        'refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'change_password/',
        views.ChangePasswordView.as_view(),
        name='change_password'),
    path(
        'forgot_password/',
        views.ForgotPasswordView.as_view()),
    path(
        'forgot_password_complete/',
        views.ForgotPasswordCompleteView.as_view()),
    path(
        'profile/<int:pk>/',
        views.ProfileView.as_view()),
    path(
        'user_list',
        views.ListOfUsers.as_view()),
]
