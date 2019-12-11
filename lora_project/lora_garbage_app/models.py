from django.db import models

# Create your models here.
class TrashInfo(models.Model):
    tlocationx = models.IntegerField()
    tlocationy = models.IntegerField()
