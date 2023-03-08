from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'is_staff',
        'is_mentor',
        'username',
        'name',
        'last_name')
    list_filter = ['is_staff', 'is_mentor', 'is_fireman']
