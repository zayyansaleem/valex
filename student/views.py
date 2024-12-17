from django.shortcuts import render
from student.models import Student

# Create your views here.


def post_student(request):
    if request.method == 'POST':
        obj = Student()
        obj.name = request.POST.get('stname')
        obj.age = request.POST.get('age')
        obj.department = request.POST.get('dept')
        obj.phone = request.POST.get('phone')
        obj.email = request.POST.get('email')
        obj.username = request.POST.get('uname')
        obj.address = request.POST.get('addr')
        obj.password = request.POST.get('psw')
        obj.save()
    return render(request,'student/student.html')


def view_student(request):
    obj = Student.objects.all()
    context = {
        'x': obj
    }
    return render(request,'student/view_student.html',context)

