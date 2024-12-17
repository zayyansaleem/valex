from django.conf.urls import url
from marklist import views

urlpatterns = [
    url('post_marklist/', views.post_marklist),
    url('view_marklist/', views.view_marklist)

]