from django.contrib import admin

from apps.questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
