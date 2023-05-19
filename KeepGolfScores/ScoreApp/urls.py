from django.urls import re_path as url
from ScoreApp import views

urlpatterns=[
    url(r'^courses$',views.courseApi),
    url(r'^courses/([0-9]+)$',views.courseApi)
]