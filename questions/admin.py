from django.contrib import admin

from .models import Tag, Question


@admin.register(Tag)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    ordering = ['-title', ]


@admin.register(Question)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'tags', 'created_at')
    search_fields = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at', 'title']

    def tags(self, obj):
        return ', '.join(tag.title for tag in obj.tag.all())
