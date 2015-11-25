# Register your models here.

from django.contrib import admin
from userprofile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'first_name', 'last_name', 'middle_name', 'rate', 'date_joined',
              'is_staff', 'is_active']
    list_filter = ['date_joined']



admin.site.register(UserProfile, UserProfileAdmin)