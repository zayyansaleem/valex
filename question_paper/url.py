from django.conf.urls import url
from question_paper import views

urlpatterns = [
    url('post_questionpaper/', views.post_questionpaper),
    url('view_questionpaper/', views.view_questionpaper)
]