from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def educateandempower(request):
    return render(request,"educateandempower.html")

