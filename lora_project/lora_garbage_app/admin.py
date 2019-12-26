from django.contrib import admin
from lora_garbage_app.models import TrashHistory,TrashInfo
# Register your models here.
class TrashHistoryAdmin(admin.ModelAdmin):
    list_display = ('trash_can_name','trash_history_weight','trash_history_height',)

admin.site.register(TrashHistory,TrashHistoryAdmin)
admin.site.register(TrashInfo)