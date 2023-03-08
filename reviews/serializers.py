from rest_framework import serializers

from .models import AnswerReview, QuestionReview, CommentReview


class AnswerReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = AnswerReview
        fields = '__all__'


class QuestionReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = QuestionReview
        fields = '__all__'


class CommentReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = CommentReview
        fields = '__all__'
