from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.student_detail, name='student_detail')
]