from django.contrib import admin
from . models import UserProfile, Profile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user','first_name','last_name', 'email', 'birth_date', 'city', 'phone','country','hobby','bio','photo']

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Profile, UserProfileAdmin)


admin.site.site_header = 'Administration'

