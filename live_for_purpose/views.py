
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView

from live_for_purpose.forms import CommentModelForm
from .models import Post, Comments
from . import urls
# Create your views here.

def index(request):
    return render(request,"index.html")

def educateandempower(request):
    return render(request,"educateandempower.html")


def donate(request):
    return render(request,"donate.html")


def aboutus(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")




class blogView(ListView):
    model = Post
    template_name="blog.html"

#class articleView(DetailView):
    #model= Blog
    #template_name="openpost.html"
    #def get_user_profile(self,pk):
        #return get_object_or_404(Blog,pk=pk)
class articleView(DetailView):
    model=Post
    template_name="openpost.html"

class addcommentView(CreateView):
    model=Comments
    form_class=CommentModelForm
    template_name='add_comment.html'
    #fields="__all__"
    
    def form_valid(self, form):
        form.instance.comm_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('index')
        

