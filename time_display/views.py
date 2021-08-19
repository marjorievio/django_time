from django.shortcuts import render, redirect, HttpResponse 
from time import gmtime, strftime, localtime
import time

# Create your views here.
def root(request):
    return redirect('/time_display')

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "timelocal": strftime("%d-%m-%y %H:%M", localtime())
    }
    return render(request, 'index.html' , context)