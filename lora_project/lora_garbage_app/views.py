from django.shortcuts import render,redirect
from . import models
from . import trash_collection
from django.http import HttpResponse
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

def path_generate(request):
    if request.method == 'POST':
        if request.POST.get('start_location'):
            # print(request.POST.get('start_location'))
            start_trash_can = models.TrashInfo.objects.get(id=request.POST.get('start_location'))
            other_trash_cans = models.TrashInfo.objects.exclude(id= request.POST.get('start_location'))

            # start 座標
            print("====最佳路徑程式開始====")

            start = (start_trash_can.tlocation_x,start_trash_can.tlocation_y)
            print("起點為" + start_trash_can.tloaction_name + "座標為" + str(start))

            # 其他座標
            vertices = {}
            for other_trash_can in other_trash_cans:
                coordinate = (other_trash_can.tlocation_x,other_trash_can.tlocation_y)
                vertices[coordinate] = (other_trash_can.tlocation_weight,other_trash_can.tlocation_hight)

            # 印出其他座標資料
            print(vertices)

            # 呼叫勝安trash_collectionAPI
            path_handler = trash_collection.collect_trash()
            output = path_handler.setting(start, vertices)

            # 輸出 output
            print(output)
            print("====最佳路徑程式結束====")
            return redirect(index)
        else:
            return redirect(index)