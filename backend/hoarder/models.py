from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    subreddit = models.CharField(max_length=21)
    url = models.URLField()
    cdt = models.DateTimeField()
    is_saved = models.BooleanField(default=True)
    nsfw = models.BooleanField(default = False)

    def _str_(self):
        return self.title