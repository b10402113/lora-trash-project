from django.contrib import admin
from lora_garbage_app.models import TrashHistory,TrashInfo
# Register your models here.
admin.site.register(TrashHistory)
admin.site.register(TrashInfo)