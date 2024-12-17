from django.shortcuts import render
from doubts.models import Doubts
from datetime import datetime

# Create your views here.
def post_doubts(request):
    if request.method == 'POST':
        obj = Doubts()
        obj.doubt = request.POST.get('doubts')
        obj.student_id=1
        obj.response = 'pending'
        obj.date = datetime.today()
        obj.time = datetime.now()
        obj.save()
    return render(request,'doubts/doubts.html')


def post_response(request,idd):
    if request.method == 'POST':
        obj = Doubts.objects.get(doubt_id=idd)
        obj.response = request.POST.get('complaint')
        obj.save()
    return render(request,'doubts/post_response.html')

def doubtsandresponse(request):
    obj = Doubts.objects.all()
    context = {
        'a': obj
    }
    return render(request,'doubts/doubt&response.html',context)

def view_replay(request):
    obj = Doubts.objects.all()
    context = {
        'a': obj
    }
    return render(request,'doubts/view_replay.html',context)