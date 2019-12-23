from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request, 'index.html')

def distrubution(request):
    return render(request, 'index.html')

def overview(request):
    trash_cans = models.TrashInfo.objects.all()

    return render(request, 'overview.html',locals())

def trash_detail(request,trash_id):
    trash_can = models.TrashInfo.objects.get(id=trash_id)
    trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)

    return render(request, 'trash_detail.html',locals())