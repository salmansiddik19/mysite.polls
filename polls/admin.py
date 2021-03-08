from django.contrib import admin
from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
