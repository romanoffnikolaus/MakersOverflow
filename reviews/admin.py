from django.contrib import admin

from .models import QuestionReview, AnswerReview, CommentReview

admin.site.register(QuestionReview)
admin.site.register(AnswerReview)
admin.site.register(CommentReview)
