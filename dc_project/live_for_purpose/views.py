from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def educateandempower(request):
    return render(request,"educateandempower.html")

def aboutus(request):
    return render(request,"aboutus.html")

def blog(request):
    return render(request,"blog.html")

def openpost(request):
    return render(request,"openpost.html")

    