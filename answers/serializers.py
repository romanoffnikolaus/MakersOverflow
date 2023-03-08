from rest_framework import serializers

from .models import Answer, Comment
from reviews.models import AnswerReview, CommentReview
from reviews.serializers import AnswerReviewSerializer, CommentReviewSerializer
from questions.utils import filter_text


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Answer
        fields = '__all__'

    def validate_body(self, body):
        body = filter_text(body)
        return body

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        answer = Answer.objects.create(author=user, **validated_data)
        return answer

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(
            Comment.objects.filter(answer=instance.pk), many=True).data
        representation['likes'] = sum(
            1 for i in AnswerReviewSerializer(
                AnswerReview.objects.filter(
                    answer=instance.pk,
                    is_liked=True),
                many=True).data)
        representation['dislikes'] = sum(
            1 for i in AnswerReviewSerializer(
                AnswerReview.objects.filter(
                    answer=instance.pk,
                    is_liked=False),
                many=True).data)
        try:
            request = self.context.get('request')
            user = request.user
            review = AnswerReview.objects.filter(answer=instance, author=user).first()
            if review:
                representation['isLiked'] = True if review.is_liked else False
            else:
                representation['isLiked'] = None
        except:
            pass
        return representation


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Comment
        fields = '__all__'

    def validate_body(self, body):
        body = filter_text(body)
        return body

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = sum(
            1 for i in CommentReviewSerializer(
                CommentReview.objects.filter(
                    comment=instance.pk,
                    is_liked=True),
                many=True).data)
        representation['dislikes'] = sum(
            1 for i in CommentReviewSerializer(
                CommentReview.objects.filter(
                    comment=instance.pk,
                    is_liked=False),
                many=True).data)
        return representation
