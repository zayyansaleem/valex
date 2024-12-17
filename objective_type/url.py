from django.conf.urls import url
from objective_type import views

urlpatterns = [
    url('post_objectivetype/', views.post_objectivetype),
    url('view_objectivetype/', views.view_objectivetype)
]