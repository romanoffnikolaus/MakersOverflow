from django.urls import path

from . import views


urlpatterns = [
    path('answers/', views.AnswerCreateView.as_view()),
    path('answers/<int:pk>/', views.AnswerDetailView.as_view()),
    path('comments/', views.CommentCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]
