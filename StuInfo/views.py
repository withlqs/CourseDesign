from django.shortcuts import *
from django.http import *
import datetime

# Create your views here.

def search_form(request):
    return render_to_response('search_form.html');

def index(request):
    return render_to_response('index.html', {'current_date': datetime.datetime.now()})

def hello(request):
    return HttpResponse("Hello")

def time(request):
    assert False;
    return HttpResponse(datetime.datetime.now())
