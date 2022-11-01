from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    subreddit = models.CharField(max_length=21)
    url = models.URLField()
    creation_date_time = models.DateTimeField()
    is_saved = models.BooleanField(default=True)
    over_18 = models.BooleanField()

    def _str_(self):
        return self.title