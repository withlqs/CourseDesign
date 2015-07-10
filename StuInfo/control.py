#-*- coding: UTF-8 -*- 
from StuInfo.models import Student
from StuInfo.forms import AddForm

def FormToModel(form):
    cleaned_data = form.cleaned_data;
    return Student(
            StudentID = cleaned_data['StudentID'],
            Name = cleaned_data['Name'],
            PhoneNumber = cleaned_data['PhoneNumber'], 
            Email = cleaned_data['Email'],
            Address = cleaned_data['Address'],
            Birthday = cleaned_data['Birthday']
            )

def ModelToForm(model):
    return AddForm(
            initial = {
                'StudentID': model.StudentID,
                'Name': model.Name,
                'PhoneNumber': model.PhoneNumber,
                'Email': model.Email,
                'Address': model.Address,
                'Birthday': model.Birthday
                }
            )

