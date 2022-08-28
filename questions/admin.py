from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'answer', 'user_id', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'user_id', 'created_at')
    search_fields = ('title', 'answer')

