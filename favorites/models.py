from django.db import models
from django.contrib.auth import get_user_model

from answers.models import Question


User = get_user_model()


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.question
