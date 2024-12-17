from django.conf.urls import url
from schedule import views

urlpatterns = [
    url('post_schedule/', views.post_schedule),
    url('view_schedule/', views.view_schedule),
    url('manage_schedule/', views.manage_schedule),
    url('view_apply_exam/', views.view_apply_exam)
]