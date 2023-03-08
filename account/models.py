from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from slugify import slugify


class UserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create(email, password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()


class User(AbstractUser):
    objects = UserManager()
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = None
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    activation_code = models.CharField(max_length=10, null=True)
    user_photo = models.ImageField(upload_to='account/', blank=True)
    github_account = models.URLField(blank=True)
    web_site = models.URLField(blank=True)
    telegram_account = models.URLField(blank=True)
    is_recognized_member = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)
    is_mentor = models.BooleanField(default=False)
    is_fireman = models.BooleanField(default=False)
    about_me = models.TextField(default='shy user')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def create_activation_code(self):
        code = get_random_string(10)
        self.activation_code = code
        self.save()
