"""valex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('answer_sheet/', include('answer_sheet.url')),
    url('application/', include('application.url')),
    url('complaint/', include('complaint.url')),
    url('doubts/', include('doubts.url')),
    url('examiner/', include('examiner.url')),
    url('feedback/', include('feedback.url')),
    url('login/', include('login.url')),
    url('marklist/', include('marklist.url')),
    url('notification/', include('notification.url')),
    url('objective_type/', include('objective_type.url')),
    url('schedule/', include('schedule.url')),
    url('student/', include('student.url')),
    url('question_paper/', include('question_paper.url'))
]