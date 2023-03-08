from rest_framework import generics

from .serializers import AnswerSerializer, CommentSerializer
from .models import Answer, Comment
from .permissions import IsAdminAuthPermission, IsOwnerOrAdminOnly


class AnswerCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminAuthPermission]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdminOnly]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminAuthPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdminOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
