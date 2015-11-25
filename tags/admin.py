from django.contrib import admin
from models import Tag
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    fields = ['tag']
    list_filter = ['tag']


admin.site.register(Tag, TagAdmin)