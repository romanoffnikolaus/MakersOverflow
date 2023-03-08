from rest_framework import serializers

from .models import Tag, Question
from answers.models import Answer
from answers.serializers import AnswerSerializer
from favorites.models import Favorites
from favorites.serializers import FavoritesSerializer

from .utils import filter_text


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answers_count'] = instance.answers.count()
        return representation


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Question
        fields = '__all__'

    def validate_title(self, title):

        if self.Meta.model.objects.filter(title=title).exists():
            raise serializers.ValidationError('Такой заголовок уже существует')
        return title

    def validate_body(self, body):
        body = filter_text(body)
        return body

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['favorite'] = (
            i['is_favorite'] for i in FavoritesSerializer(
                Favorites.objects.filter(
                    is_favorite=True,
                    question=instance.pk),
                many=True).data)
        representation['answers'] = AnswerSerializer(Answer.objects.filter(
            question=instance.pk), many=True, context=self.context).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        tag = validated_data.pop('tag', [])
        post = Question.objects.create(author=user, **validated_data)
        post.tag.add(*tag)
        return post
