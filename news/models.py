from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=1000)
    url = models.URLField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title
