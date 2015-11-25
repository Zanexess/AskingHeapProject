from django.contrib import admin
from models import LikeToQuestion, LikeToAnswer, LikeToUser

# Register your models here.
class LikeToQuestionAdmin(admin.ModelAdmin):
    fields = ['like_author', 'to_question', 'value']
    list_filter = ['to_question']


class LikeToAnswerAdmin(admin.ModelAdmin):
    fields = ['like_author', 'to_answer', 'value']
    list_filter = ['to_answer']

class LikeToUserAdmin(admin.ModelAdmin):
    fields = ['like_author', 'to_user', 'value']
    list_filter = ['to_user']

admin.site.register(LikeToAnswer, LikeToAnswerAdmin)
admin.site.register(LikeToQuestion, LikeToQuestionAdmin)
admin.site.register(LikeToUser, LikeToUserAdmin)
