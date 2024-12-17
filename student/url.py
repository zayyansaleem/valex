from django.conf.urls import url
from student import views

urlpatterns = [
    url('post_student/', views.post_student),
    url('view_student/', views.view_student)

]