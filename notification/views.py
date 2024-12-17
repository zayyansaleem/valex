from django.shortcuts import render
from notification.models import Notification
import datetime
# Create your views here.


def post_notification(request):
    if request.method == 'POST':
        obj = Notification()
        obj.notification = request.POST.get('notification')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request,'notification/notification.html')


def view_notification(request):
    obj = Notification.objects.all()
    context = {
        'x': obj
    }
    return render(request,'notification/view_notification.html',context)
