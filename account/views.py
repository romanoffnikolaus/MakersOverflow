from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from slugify import slugify
from rest_framework.permissions import AllowAny

from . import serializers as s
from . import permissions as p
from .permissions import IsOwnerOrReadOnly


User = get_user_model()


class RegistrationView(generics.CreateAPIView):
    serializer_class = s.RegistrationSerializer

    @swagger_auto_schema(request_body=s.RegistrationSerializer())
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(
            email=email,
            activation_code=activation_code).first()  # берем первого юзера
        if not user:
            return Response('Пользователь не найден', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активирован', status=200)


class ChangePasswordView(APIView):
    permission_classes = [p.IsActivePermission]

    @swagger_auto_schema(request_body=s.ChangePasswordSerializer)
    def post(self, request):
        serializer = s.ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен', status=200)


class ForgotPasswordView(APIView):
    @swagger_auto_schema(request_body=s.ForgotPasswordSerializer)
    def post(self, request):
        serializer = s.ForgotPasswordSerializer(
            data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response(
                'Вам выслали сообщение для восстановления пароля'

            )


class ForgotPasswordCompleteView(APIView):
    @swagger_auto_schema(request_body=s.ForgotPasswordCompleteSerializer)
    def post(self, request):
        serializer = s.ForgotPasswordCompleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response(
                'Ваш пароль успешно восстановлен'
            )


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = s.ProfileSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if not request.user.is_staff:
            serializer.validated_data.pop('is_mentor', None)
        # if request.user.username != serializer.validated_data['username']:
        #     instance.slug = slugify(serializer.validated_data['username'])
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in ['GET']:
            permissions = [AllowAny]
        else:
            permissions = [IsOwnerOrReadOnly]
        return [permission() for permission in permissions]


class ListOfUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = s.ProfileSerializer


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        username = request.data.get('username')
        user = User.objects.get(username=username)
        user_data = {'id': user.id,
                     'name': user.name,
                     'last_name': user.last_name,
                     'github_account': user.github_account,
                     'telegram_account': user.telegram_account,
                     'web_site': user.web_site,
                     'email': user.email,
                     'date_joined': user.date_joined}
        new_data = list(user_data.items())
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        serializer.validated_data.update(new_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
