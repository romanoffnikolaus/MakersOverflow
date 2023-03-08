from django.urls import path, include

from . import views

urlpatterns = [
    path('answer-reviews/', views.AnswerReviewListView.as_view()),
    path('question-reviews/', views.QuestionReviewListView.as_view()),
    path('answers/<int:pk>/like/', views.answer_like),
    path('comments/<int:pk>/like/', views.comment_like),
]
