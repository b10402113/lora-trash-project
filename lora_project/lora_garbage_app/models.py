from django.db import models

# Create your models here.
class TrashInfo(models.Model):

    tloaction_name = models.CharField(null=False,max_length=100)
    tlocation_x = models.IntegerField()
    tlocation_y = models.IntegerField()
    tlocation_weight = models.IntegerField()
    tlocation_hight = models.IntegerField()
    tpub_date = models.DateField(null=False)

class TrashHistory(models.Model):
    trash_history_weight  = models.IntegerField()
    trash_history_height = models.IntegerField()
    trash_can_name = models.ForeignKey(TrashInfo,on_delete=models.CASCADE)
