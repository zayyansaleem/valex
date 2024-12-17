from django.shortcuts import render
from application.models import Application

# Create your views here.

def view_application(request):
    obj = Application.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'application/view_application.html',context)


def manage_application(request):
    obj = Application.objects.all()
    context = {
        'x': obj
    }
    return render(request, 'application/view_m_application.html',context)

