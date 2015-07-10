#-*- coding: UTF-8 -*- 
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from StuInfo.models import *
from datetime import date

YearChoice = []

for y in range(1990, int(date.today().year)+1):
    YearChoice.append(str(y))

class AddForm(forms.Form):
    StudentID = forms.CharField(label = '学号', max_length = Student.StudentIDMaxLen)
    Name = forms.CharField(label = '姓名', max_length = Student.NameMaxLen)
    PhoneNumber = forms.CharField(label = '电话', max_length = Student.PhoneNumberMaxLen)
    Email = forms.EmailField(label = 'E-mail')
    Address = forms.CharField(label = '地址', max_length = Student.AddressMaxLen, widget=forms.Textarea)
    Birthday = forms.DateField(label = '生日', widget=SelectDateWidget(years = YearChoice))

class SearchForm(forms.Form):
    StudentID = forms.CharField(label = '学号', max_length = Student.StudentIDMaxLen)
    Name = forms.CharField(label = '姓名', max_length = Student.NameMaxLen)
    PhoneNumber = forms.CharField(label = '电话', max_length = Student.PhoneNumberMaxLen)
    Email = forms.EmailField(label = 'E-mail')
    Address = forms.CharField(label = '地址', max_length = Student.AddressMaxLen, widget=forms.Textarea)
    Birthday = forms.DateField(label = '生日', widget=SelectDateWidget(years = YearChoice))

