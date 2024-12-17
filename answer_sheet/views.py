from django.shortcuts import render
from answer_sheet.models import AnswerSheet
import datetime
# Create your views here.


def post_answersheet(request):
    if request.method == 'POST':
        obj = AnswerSheet()
        obj.answer_sheet = request.POST.get('asheet')
        obj.student_id = 1
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()

    return render(request,'answer_sheet/answersheet.html')


def view_answer(request):
    obj=AnswerSheet.objects.all()
    context={
        'x':obj
    }
    return render(request,'answer_sheet/viewanswersheet.html', context)
