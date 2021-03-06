#-*- coding: UTF-8 -*- 
import os
from django.shortcuts import *
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.db import IntegrityError
from StuInfo import forms
from StuInfo import models
from StuInfo import control
from django.contrib.auth import views
from CourseDesign.settings import BASE_DIR
import datetime
import xlwt3
import random

# Create your views here.

def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/?pure=1')
    return views.login(request)

def sidebar(request):
    if request.user.is_authenticated():
        return render_to_response('sidebar.html', {
            'logined': True,
            'user': request.user.username
            }, context_instance=RequestContext(request))
    return render_to_response('sidebar.html', {
        'logined': False,
        }, context_instance=RequestContext(request))


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect('/accounts/login/')

def logined(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/search/')
    return HttpResponseRedirect('/accounts/login/')

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1']))
            return HttpResponseRedirect('/successful/?op=reg')
    else:
        form = UserCreationForm()
    return render_to_response('registration/register.html', {
        'form': form,
        }, context_instance=RequestContext(request))

def add(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            info = control.FormToModel(form)
            try:
                info.save()
            except IntegrityError:
                return render_to_response('duplicate.html', {})
            return HttpResponseRedirect('/successful/?op=add')
    else:
        form = forms.AddForm()
    return render_to_response('add.html', {
        'form': form,
        'user': request.user.username
        }, context_instance=RequestContext(request))

def delete(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if request.method == 'GET':
        query_set = models.Student.objects.filter(StudentID=request.GET['StudentID'])
        if query_set:
            query_set.delete()
            return HttpResponseRedirect('/successful/?op=del')
    raise Http404

def modify(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if request.method == 'GET':
        query_set = models.Student.objects.filter(StudentID=request.GET['StudentID'])
        if query_set:
            form = control.ModelToForm(query_set[0])
            return render_to_response('modify.html', {
                'form': form
                }, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = forms.AddForm(request.POST)
        if form.is_valid():
            models.Student.objects.filter(StudentID=request.POST['StudentID']).delete()
            info = control.FormToModel(form)
            try:
                info.save()
            except IntegrityError:
                return render_to_response('duplicate.html', {
                    'user': request.user.username
                    })
            return HttpResponseRedirect('/successful/?op=mod')
        else:
            form.fields['StudentID'].widget.attrs['readonly'] = True
            return render_to_response('modify.html', {
                'form': form
                }, context_instance=RequestContext(request))
    raise Http404

def search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if not request.method == 'GET':
        raise Http404
    op = {
            'add': '添加',
            'del': '删除',
            'mod': '修改',
            'reg': '注册'
            }
    try:
        op_get = request.GET['op']
    except MultiValueDictKeyError:
        return render_to_response('search.html', {}, context_instance=RequestContext(request))
    if not op_get in op:
        raise Http404
    return render_to_response('search.html', {
        'user': request.user.username,
        'op': op[op_get]
        }, context_instance=RequestContext(request))
def getXls(infoList):
    """ElementList = ['StudentID', 'Name', 'PhoneNumber', 'Email', 'Address', 'Birthday']"""
    wb = xlwt3.Workbook()
    sheet = wb.add_sheet("查询结果")
    sheet.write(0, 0, "学号")
    sheet.write(0, 1, "姓名")
    sheet.write(0, 2, "电话")
    sheet.write(0, 3, "电子邮箱")
    sheet.write(0, 4, "地址")
    sheet.write(0, 5, "出生日期")
    for i in range(0, len(infoList)):
        sheet.write(i+1, 0, infoList[i].StudentID)
        sheet.write(i+1, 1, infoList[i].Name)
        sheet.write(i+1, 2, infoList[i].PhoneNumber)
        sheet.write(i+1, 3, infoList[i].Email)
        sheet.write(i+1, 4, infoList[i].Address)
        sheet.write(i+1, 5, str(infoList[i].Birthday))

    fileName = str(random.randint(1, 10000000))+'.xls'
    path = os.path.join(BASE_DIR, "StuInfo/static/"+fileName).replace('\\', '/')
    wb.save(path)
    return "/static/"+fileName

def view(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
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
        xls_url = getXls(render_list)
        return render_to_response('view.html', {
            'render_list': render_list,
            'user': request.user.username,
            'xls': getXls(render_list)
            }, context_instance=RequestContext(request))

    if request.method == 'GET':
        if request.GET['all'] == "1":
            render_list = []
            for item in list(models.Student.objects.all()):
                render_list.append(item)
            return render_to_response('view.html', {
                'render_list': render_list,
                'user': request.user.username,
                'xls': getXls(render_list)
                }, context_instance=RequestContext(request))
    raise Http404

def successful(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    if request.method != 'GET':
        raise Http404
    op = {
            'add': '添加',
            'del': '删除',
            'mod': '修改',
            'reg': '注册'
            }
    try:
        op_get = request.GET['op']
    except MultiValueDictKeyError:
        raise Http404
    if not request.GET['op'] in op:
        raise Http404
    return render_to_response('successful.html', {
        'user': request.user.username,
        'operation': op[request.GET['op']]
        }, context_instance=RequestContext(request))

def index(request):
    """if not request.user.is_authenticated():
       return HttpResponseRedirect('/accounts/login/')"""
    if request.method == 'GET':
        if 'pure' in request.GET:
            return render_to_response('pure.html', {
                'current_date': datetime.datetime.now()
                }, context_instance=RequestContext(request))
    return render_to_response('index.html', {
        'current_date': datetime.datetime.now()
        }, context_instance=RequestContext(request))
