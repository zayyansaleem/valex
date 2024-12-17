from django.shortcuts import render
from marklist.models import Marklist
import datetime
# Create your views here.


def post_marklist(request):
    if request.method == 'POST':
        obj = Marklist()
        obj.marklist = request.POST.get('mlist')
        obj.application_id = 1
        obj.student_id = 1
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()

    return render(request, 'marklist/marklist.html')


def view_marklist(request):
    obj = Marklist.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'marklist/view_marklist.html',context)
