#-*- coding: UTF-8 -*- 
from django.shortcuts import *
from django.http import *
from StuInfo import forms
from StuInfo import models
from StuInfo import control
import datetime

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            info = control.FormToModel(form)
            info.save()
            return HttpResponseRedirect('/successful/')
    else:
        form = forms.AddForm()

    return render_to_response('add.html', {'form': form})

def delete(request):
    if request.method == 'GET':
        query_set = models.Student.objects.filter(StudentID=request.GET['StudentID'])
        if query_set:
            query_set.delete()
            return HttpResponseRedirect('/successful/')

    raise Http404

def modify(request):
    if request.method == 'GET':
        query_set = models.Student.objects.filter(StudentID=request.GET['StudentID'])
        if query_set:
            form = control.ModelToForm(query_set[0])
            return render_to_response('modify.html', {'form': form})
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            models.Student.objects.filter(StudentID=request.POST['StudentID']).delete()
            info = control.FormToModel(form)
            info.save()
            return HttpResponseRedirect('/successful/')
    raise Http404

def search(request):
    return render_to_response('search.html')

def view(request):
    if request.method == 'POST':
        remain = models.Student.objects

        """ElementList = ['StudentID', 'Name', 'PhoneNumber', 'Email', 'Address', 'Birthday']"""

        if request.POST.getlist('StudentIDEnable'):
            if request.POST.getlist('StudentIDPart'):
                remain = remain.filter(StudentID__icontains=request.POST['StudentID'])
            else:
                remain = remain.filter(StudentID=request.POST['StudentID'])
        if request.POST.getlist('NameEnable'):
            if request.POST.getlist('NamePart'):
                remain = remain.filter(Name__icontains=request.POST['Name'])
            else:
                remain = remain.filter(Name=request.POST['Name'])
        if request.POST.getlist('PhoneNumberEnable'):
            if request.POST.getlist('PhoneNumberPart'):
                remain = remain.filter(PhoneNumber__icontains=request.POST['PhoneNumber'])
            else:
                remain = remain.filter(PhoneNumber=request.POST['PhoneNumber'])
        if request.POST.getlist('EmailEnable'):
            if request.POST.getlist('EmailPart'):
                remain = remain.filter(Email__icontains=request.POST['Email'])
            else:
                remain = remain.filter(Email=request.POST['Email'])
        if request.POST.getlist('AddressEnable'):
            if request.POST.getlist('AddressPart'):
                remain = remain.filter(Address__icontains=request.POST['Address'])
            else:
                remain = remain.filter(Address=request.POST['Address'])
        if request.POST.getlist('BirthdayEnable'):
            if request.POST.getlist('BirthdayPart'):
                remain = remain.filter(Birthday__icontains=request.POST['Birthday'])
            else:
                remain = remain.filter(Birthday=request.POST['Birthday'])

        render_list = []
        for item in list(remain.all()):
            render_list.append(item)
        return render_to_response('view.html', {'render_list': render_list})
    else:
        raise Http404


def successful(request):
    return render_to_response('successful.html')

def index(request):
    return render_to_response('index.html', {'current_date': datetime.datetime.now()})
