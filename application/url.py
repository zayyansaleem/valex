from django.conf.urls import url
from application import views

urlpatterns = [
    url('view_application/', views.view_application),
    url('manage_application/', views.manage_application)

]