from django.shortcuts import render
from question_paper.models import QuestionPaper
import datetime
# Create your views here.


def post_questionpaper(request):
    if request.method == 'POST':
        obj = QuestionPaper()
        obj.schedule_id = 1
        obj.question_paper = request.POST.get('qpaper')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request, 'question_paper/QUESTIONPAPER.html')


def view_questionpaper(request):
    obj = QuestionPaper.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'question_paper/view_questionpaper.html',context)
