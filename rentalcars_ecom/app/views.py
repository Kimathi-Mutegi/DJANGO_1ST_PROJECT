from django.shortcuts import render
from urllib import request

# Create your views here.
def home(request):
    return render(request, "app/base.html")
