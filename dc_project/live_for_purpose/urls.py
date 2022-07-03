

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("educateandempower", views.educateandempower,name="educateandempower"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("blog", views.blog, name="blog"),
    path("openpost", views.openpost, name="openpost"),


]
