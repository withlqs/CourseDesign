from StuInfo.models import Student

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


