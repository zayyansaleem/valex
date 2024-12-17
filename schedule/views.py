from django.shortcuts import render
from schedule.models import Schedule
# Create your views here.


def post_schedule(request):
    if request.method == 'POST':
        obj = Schedule()
        obj.exam_name = request.POST.get('ename')
        obj.exam_date = request.POST.get('date')
        obj.exam_time = request.POST.get('time')
        obj.save()
    return render(request, 'schedule/schedule.html')


def view_schedule(request):
    obj = Schedule.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'schedule/view_schedule.html',context)


def manage_schedule(request):
    obj = Schedule.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'schedule/view_m_schedule.html',context)


def view_apply_exam(request):
    obj = Schedule.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'schedule/view exam&applyexam.html',context)
