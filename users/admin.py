from django.contrib import admin
from users.models import *
from django.contrib.auth.models import Group





admin.site.site_header = 'GitHub Users Dashbaord'


class api_callsAdmin(admin.ModelAdmin):
	list_display = ('username_filter','min_followers_filter','min_repos_filter','location_filter','inserted_datetime',)
	list_filter = ('inserted_datetime',)

class user_datasAdmin(admin.ModelAdmin):
	list_display = ('login','user_id','name','location','email','public_repos','followers','following','inserted_datetime','thumbnail',)
	list_filter = ('inserted_datetime',)
	search_fields = ('name', 'followers', 'public_repos', 'location','email','inserted_datetime',)

admin.site.register(api_calls,api_callsAdmin)
admin.site.register(user_data,user_datasAdmin)
admin.site.unregister(Group)
# Register your models here.
