from django.shortcuts import render,redirect
from . import models
from . import trash_collection
import json
import cv2
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
from . import map
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
def index(request,location = 'T4'):
    trash_cans = models.TrashInfo.objects.all()
    return render(request, 'index.html',locals())

def distrubution(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def overview(request):
    trash_cans = models.TrashInfo.objects.all()

    return render(request, 'overview.html',locals())

def event(request):
    trash_cans = models.TrashInfo.objects.all()
    return render(request, 'event.html', locals())

def trash_detail(request,trash_id):
    trash_can = models.TrashInfo.objects.get(id=trash_id)
    hnumber = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name).count()
    if hnumber > 10:
        trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)[hnumber-10:hnumber]
    else:
        trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)

    tweight = []
    theight = []
    times = []
    hour_data = []
    hour_dict={}
    hour_dict2={}
    hour_dict_height={}
    for trash in trash_infomation:
        tweight.append(trash.trash_history_weight)
        theight.append(trash.trash_history_height)
        times.append(trash.trash_history_time.strftime("%H時%M分%S秒"))

        hour_data.append((trash.trash_history_time.hour,trash.trash_history_weight,trash.trash_history_height))
    for i in range(1,25):
        hour_dict[str(i)] = [0,0,0]
    for (hour,weight,height) in hour_data:
        hour_dict[str(hour)][0] += 1
        hour_dict[str(hour)][1] += weight
        hour_dict[str(hour)][2] += height
        #     算出平均值
    for i in range(1, 25):
        if hour_dict[str(i)][0] != 0 and hour_dict[str(i)][1] != 0:
            num = hour_dict[str(i)][0]
            hour_dict[str(i)][0] = hour_dict[str(i)][1]/num
            if hour_dict[str(i)][2] != 0:
                hour_dict[str(i)][2] = hour_dict[str(i)][2] / num

        hour_dict2[str(i)] = hour_dict[str(i)][0]
        hour_dict_height[str(i)] = hour_dict[str(i)][2]

    print(hour_dict_height)

    data = {
        "time":times,
        "weight":tweight,
        "height":theight,
        "hour_dict2":hour_dict2,
        "hour_dict_height":hour_dict_height
    }


    return render(request, 'trash_detail.html',locals())

def trash_ajax_data(request,trash_id):
    trash_can = models.TrashInfo.objects.get(id=trash_id)
    hnumber = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name).count()
    if hnumber > 10:
        trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)[hnumber-10:hnumber]
    else:
        trash_infomation = models.TrashHistory.objects.filter(trash_can_name__tloaction_name=trash_can.tloaction_name)
    weight_now = trash_can.tlocation_weight
    height_now = trash_can.tlocation_hight
    tweight = []
    theight = []
    times = []
    hour_data = []
    hour_dict={}
    hour_dict2={}
    hour_dict_height={}
    for trash in trash_infomation:
        tweight.append(trash.trash_history_weight)
        theight.append(trash.trash_history_height)
        times.append(trash.trash_history_time.strftime("%H時%M分%S秒"))

        hour_data.append((trash.trash_history_time.hour,trash.trash_history_weight,trash.trash_history_height))
    for i in range(1,25):
        hour_dict[str(i)] = [0,0,0]
    for (hour,weight,height) in hour_data:
        hour_dict[str(hour)][0] += 1
        hour_dict[str(hour)][1] += weight
        hour_dict[str(hour)][2] += height
        #     算出平均值
    for i in range(1, 25):
        if hour_dict[str(i)][0] != 0 and hour_dict[str(i)][1] != 0:
            num = hour_dict[str(i)][0]
            hour_dict[str(i)][0] = hour_dict[str(i)][1]/num
            if hour_dict[str(i)][2] != 0:
                hour_dict[str(i)][2] = hour_dict[str(i)][2] / num

        hour_dict2[str(i)] = hour_dict[str(i)][0]
        hour_dict_height[str(i)] = hour_dict[str(i)][2]

    print(hour_dict_height)

    data = {
        "time":times,
        "weight":tweight,
        "height":theight,
        "hour_dict2":hour_dict2,
        "hour_dict_height":hour_dict_height,
        "weight_now":weight_now,
        "height_now":height_now
    }


    return JsonResponse(data,safe=False)

def post_trash_data(request):
    if request.method == 'POST':
        # print(request.GE)
        # json_data = json.loads(request.body)
        try:
            # json格式
            json_data = json.loads(request.body)
            trash_id = json_data["trash_id"]
            weight = json_data["weight"]  # 获取name
            height = json_data["height"]
        except:
            # 網站post
            trash_id = request.POST.get('trash_id')
            weight = request.POST.get('weight')
            height = request.POST.get('height')
        # trash_id = json_data["trash_id"]
        # weight = json_data["weight"]  # 获取name
        # height = json_data["height"]  # 获取gender
        trash_data = models.TrashHistory()
        trash_data.trash_history_height = height
        trash_data.trash_history_weight = weight
        # 獲取垃圾桶
        trash_can = models.TrashInfo.objects.get(id=trash_id)
        trash_data.trash_can_name = trash_can
        trash_can.tlocation_weight = weight
        trash_can.tlocation_hight = height
        # 判斷是否寄信
        gmail_user = 'andycheeehigh@gmail.com'
        gmail_password = 'a7935776'  # your gmail password
        if int(weight) > 2000 and trash_can.send_email_bit is False:
            trash_can.send_email_bit = True
            msg = (MIMEText('<h1>垃圾過量警告！</h1><p>地點：'+str(trash_can.tloaction_name)+'</p>重量已經超過20kg，請盡快去收垃圾！</p>','html','utf-8'))
            msg['Subject'] = 'Lora垃圾管理系統通知（請勿回覆）'
            msg['From'] = gmail_user
            msg['To'] = 'b10402113@gmail.com'
            print('===信件連結開始===')
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
            server.quit()
            print('===信件已經寄出===')
        elif int(weight) < 100 and trash_can.send_email_bit:
            trash_can.send_email_bit = False

        # 存取資料庫
        trash_can.save()
        trash_data.trash_history_time = datetime.now()
        trash_data.save()

        return redirect(event)
    else:
        return redirect(event)

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

            a = map.draw_path()
            a.start_draw(output)
            # a.map("(560,440)","(860,535)")
            a.put_text()
            return redirect(index,start_trash_can.tloaction_name)
        else:
            return redirect(index)

def display_image(request):
    fn = 'static/img/new_image.jpg'
    img = cv2.imread(fn)
    ret, jpeg = cv2.imencode('.jpg', img)
    return HttpResponse(jpeg.tostring(), content_type="multipart/x-mixed-replace")