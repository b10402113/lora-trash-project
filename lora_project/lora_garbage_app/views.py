from django.shortcuts import render
from . import models
from . import trash_collection
from django.http import HttpResponse
# trash_collection.collect_trash()
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def index(request):
    trash_cans = models.TrashInfo.objects.all()
    return render(request, 'index.html',locals())

def distrubution(request):
    return render(request, 'index.html')

def overview(request):
    trash_cans = models.TrashInfo.objects.all()

    return render(request, 'overview.html',locals())

def trash_detail(request,trash_id):
    trash_can = models.TrashInfo.objects.get(id=trash_id)
    hnumber = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name).count()
    if hnumber > 10:
        trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)[hnumber-10:hnumber]
    else:
        trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)
    tweight = []
    theight = []
    time = []
    for trash in trash_infomation:
        tweight.append(trash.trash_history_weight)
        theight.append(trash.trash_history_height)
        time.append(trash.trash_history_time.strftime("%H:%M:%S"))
    data = {
        "time":time,
        "weight":tweight,
        "height":theight
    }

    return render(request, 'trash_detail.html',locals())

def post_trash_data(request,trash_id):
    if request.method == 'POST':
        trash_id = trash_id  # 获取name
        weight = request.POST.get("weight")  # 获取name
        height = request.POST.get("height")  # 获取gender
        trash_data = models.TrashHistory()
        trash_data.trash_history_height = height
        trash_data.trash_history_weight = weight
        # 獲取垃圾桶
        trash_can = models.TrashInfo.objects.get(id=trash_id)
        trash_data.trash_can_name = trash_can
        trash_can.tlocation_weight = weight
        trash_can.tlocation_hight = height
        trash_can.save()
        trash_data.trash_history_time = datetime.now()
        trash_data.save()
        return HttpResponse("成功")
    else:
        return HttpResponse("失敗")