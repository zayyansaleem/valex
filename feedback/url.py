from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('post_feedback/', views.post_feedback),
    url('view_feedback/', views.view_feedback)

]