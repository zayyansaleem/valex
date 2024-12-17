from django.conf.urls import url
from answer_sheet import views

urlpatterns=[
    url('post_answer/', views.post_answersheet),
    url('view_sheet/', views.view_answer)

]