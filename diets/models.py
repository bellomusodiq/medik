from django.db import models

# Create your models here.


class Diet(models.Model):
    breakfast = models.CharField(max_length=400)
    lunch = models.CharField(max_length=400)
    dinner = models.CharField(max_length=400)
