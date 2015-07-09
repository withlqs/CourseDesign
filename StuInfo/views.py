from django.shortcuts import *
from django.http import *
from StuInfo.forms import *
import datetime

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
    else:
        form = AddForm()

    return render_to_response('add_form.html', {'form': form})

def successful(request):
    return render_to_response('successful.html')

def index(request):
    return render_to_response('index.html', {'current_date': datetime.datetime.now()})

def time(request):
    assert False;
    return HttpResponse(datetime.datetime.now())
