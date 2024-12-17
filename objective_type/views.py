from django.shortcuts import render
from objective_type.models import ObjectiveType
import datetime
# Create your views here.


def post_objectivetype(request):
    if request.method == 'POST':
        obj = ObjectiveType()
        obj.question_paper = request.POST.get('qs')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request, 'objective_type/objectivetype.html')


def view_objectivetype(request):
    obj = ObjectiveType.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'objective_type/view_objectivetype.html',context)
