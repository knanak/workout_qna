from django.contrib import admin
from .models import *


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 7

class IndexAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(QuestionCategory)
admin.site.register(AnswerCategory)
# admin.site.register(QuestionIndex, IndexAdmin)
admin.site.register(Question, QuestionAdmin )
admin.site.register(Result)
