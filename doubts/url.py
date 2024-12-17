from django.conf.urls import url
from doubts import views

urlpatterns = [
    url('post_doubts/', views.post_doubts),
    url('post_res/(?P<idd>\w+)', views.post_response),
    url('doubtsandresponse/', views.doubtsandresponse),
    url('view_replay/', views.view_replay),
]