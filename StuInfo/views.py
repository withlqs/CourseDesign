from django.shortcuts import *
from django.http import *
from StuInfo import forms
from StuInfo import models
from StuInfo.stuinfo_control import FormToModel
import datetime

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            info = FormToModel(form)
            info.save()
            return HttpResponseRedirect('/successful/')
    else:
        form = forms.AddForm()

    return render_to_response('add_form.html', {'form': form})

def successful(request):
    return render_to_response('successful.html')

def index(request):
    return render_to_response('index.html', {'current_date': datetime.datetime.now()})

def time(request):
    assert False;
    return HttpResponse(datetime.datetime.now())
