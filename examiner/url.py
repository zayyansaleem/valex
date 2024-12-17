from django.conf.urls import url
from examiner import views

urlpatterns = [
    url('post_examiner/', views.post_examiner),
    url('view_examiner/', views.view_examiner),
    url('manage_profile/', views.manage_profile),
    url('update_profile/', views.update_profile),
    url('update_examiner/(?P<idd>\w+)', views.update_examiner),
]