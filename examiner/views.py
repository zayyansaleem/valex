from django.shortcuts import render
from examiner.models import Examiner

# Create your views here.
def post_examiner(request):
    if request.method == 'POST':
        obj = Examiner()
        obj.username = request.POST.get('uname')
        obj.password = request.POST.get('psw')
        obj.email = request.POST.get('email')
        obj.experience = request.POST.get('exp')
        obj.name = request.POST.get('exname')
        obj.phone_number = request.POST.get('phone')
        obj.save()
    return render(request, 'examiner/examiner.html')


def view_examiner(request):
    obj = Examiner.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'examiner/view_examiner.html',context)


def manage_profile(request):
    obj = Examiner.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'examiner/manageexaminer.html',context)


def update_profile(request):
    obj = Examiner.objects.all()
    context ={
        'x' : obj
    }
    return render(request, 'examiner/updateprofile.html',context)


def update_examiner(request,idd):
    obj = Examiner.objects.filter(examiner_id=idd)
    context = {
        'x': obj
    }
    if request.method == 'POST':
        obj = Examiner.objects.get(examiner_id=idd)
        obj.username = request.POST.get('uname')
        obj.password = request.POST.get('psw')
        obj.email = request.POST.get('email')
        obj.experience = request.POST.get('exp')
        obj.name = request.POST.get('exname')
        obj.phone_number = request.POST.get('phone')
        obj.save()
    return render(request, 'examiner/update_examiner.html',context)
