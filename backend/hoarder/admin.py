from django.contrib import admin
from .models import Post

class HoarderAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'subreddit', 'url', 'cdt','is_saved', 'nsfw')

# Register your models here.
admin.site.register(Post, HoarderAdmin)
