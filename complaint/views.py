from django.shortcuts import render
from complaint.models import Complaint
import datetime
# Create your views here.


def post_complaint(request):
    if request.method == 'POST':
        obj=Complaint()
        obj.complaint = request.POST.get('complaint')
        obj.student_id = 1
        obj.reply='pending'
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.attachment = request.POST.get('ss')
        obj.save()

    return render(request, 'complaint/complaint.html')


def view_complaint(request):
    obj = Complaint.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'complaint/view_complaint.html', context)


def post_reply(request,idd):
    if request.method == 'POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.reply= request.POST.get('reply')
        obj.save()
    return render(request, 'complaint/post_reply.html')


def view_reply(request):
    obj=Complaint.objects.all()
    context={
        'a':obj
    }
    return render(request, 'complaint/view_reply.html',context)

