from django.contrib import admin
from.models import *


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(QuestionCategory)
admin.site.register(AnswerCategory)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result)

