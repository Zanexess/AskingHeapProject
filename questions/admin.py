from django.contrib import admin
from models import Answer, Question
# Register your models here.

admin.site.register(Answer)

class QuestionInline(admin.StackedInline):
    model = Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'author', 'rate', 'tags']
    inlines = [QuestionInline]
    list_filter = ['rate']

admin.site.register(Question, QuestionAdmin)