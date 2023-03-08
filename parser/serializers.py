from rest_framework import serializers


class StackOverflowSerialiser(serializers.Serializer):
    title = serializers.CharField()
    link = serializers.URLField()
