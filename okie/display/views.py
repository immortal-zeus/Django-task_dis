from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    all_things = Dis.objects.all()

    return  render(request,"display/index.html",{
        "dis":all_things
    })