from django.db import models

# Create your models here.
class Thumb(models.Model):
    uid = models.IntegerField()
    wid = models.IntegerField()

