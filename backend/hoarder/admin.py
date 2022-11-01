from django.contrib import admin
from .models import Post

class HoarderAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'subreddit', 'url', 'creation_date_time',
        'is_saved', 'over_18'
        )

# Register your models here.
admin.site.register(Post, HoarderAdmin)
