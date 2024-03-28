#polls 파일에urls.py 가 없어서 생성
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jy", views.jy, name="jy"),
    path("cafe", views.cafe, name="cafe"),

]