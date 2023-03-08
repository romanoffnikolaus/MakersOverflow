from rest_framework import serializers

from . import models
from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    question = QuestionSerializer()

    class Meta:
        model = models.Favorites
        fields = '__all__'
