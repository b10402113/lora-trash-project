from django.db import models

# Create your models here.
class TrashInfo(models.Model):

    tloaction_name = models.CharField(null=False,max_length=100,verbose_name="location_name")
    tlocation_x = models.IntegerField()
    tlocation_y = models.IntegerField()
    tlocation_weight = models.IntegerField()
    tlocation_hight = models.IntegerField()
    tpub_date = models.DateField(null=False)
    send_email_bit = models.BooleanField(default=False)

    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return str(self.tloaction_name)


class TrashHistory(models.Model):
    trash_history_weight  = models.IntegerField()
    trash_history_height = models.IntegerField()
    trash_history_time = models.DateTimeField(null=False,auto_now=True)
    trash_can_name = models.ForeignKey(TrashInfo,on_delete=models.CASCADE)

    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return str(self.trash_can_name)
