from django.db import models
from django.contrib.auth import get_user_model

from answers.models import Answer, Question, Comment

User = get_user_model()


class AnswerReview(models.Model):
    answer = models.ForeignKey(
        Answer,
        related_name='answer_reviews',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='answer_reviews',
        on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f'Answer id: {self.answer.pk}'


class QuestionReview(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='question_reviews',
        on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        related_name='question_reviews',
        on_delete=models.CASCADE
    )
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f'Question id: {self.question.pk}'


class CommentReview(models.Model):
    comment = models.ForeignKey(
        Comment,
        related_name='comment_reviews',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='comment_reviews',
        on_delete=models.CASCADE,
    )
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f'Answer id: {self.comment.pk}'
