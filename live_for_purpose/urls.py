

from django.urls import path
from . import views
from . import views
from .views import  blogView,articleView,addcommentView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index,name="index"),
    path("educateandempower", views.educateandempower,name="educateandempower"),

    path("donate", views.donate,name="donate"),

    path("aboutus", views.aboutus, name="aboutus"),
    #path("blog", views.blog, name="blog"),
    path("blog", blogView.as_view(),name="blog"),
    #path("openpost/<int:pk>", views.postcomment, name="openpost"),
    path("openpost/<int:pk>", articleView.as_view(), name="openpost"),
    path("openpost/<int:pk>/comment/add/", addcommentView.as_view(), name="add_comment"),
    path("contact", views.contact,name="contact")

]

urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)