from django import forms
from StuInfo.models import *

class AddForm(forms.Form):
    StudentID = forms.CharField(label = '学号', max_length = Student.StudentIDMaxLen)
    Name = forms.CharField(label = '姓名', max_length = Student.NameMaxLen)
    PhoneNumber = forms.CharField(label = '电话', max_length = Student.PhoneNumberMaxLen)
    Email = forms.EmailField(label = 'E-mail')
    Address = forms.CharField(label = '地址', max_length = Student.AddressMaxLen, widget=forms.Textarea)
    Birthday = forms.DateField(label = '生日')

