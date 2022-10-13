from django.contrib import admin
from .models import Manager

class HomepageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'progress')

# Register your models here.

admin.site.register(Manager, ManagerAdmin)
