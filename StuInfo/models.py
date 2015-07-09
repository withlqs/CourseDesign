from django.db import models

# Create your models here.

class Student(models.Model):
    StudentIDMaxLen = 15
    NameMaxLen = 30
    PhoneNumberMaxLen = 20
    AddressMaxLen = 100

    StudentID = models.CharField(max_length = StudentIDMaxLen)
    Name = models.CharField(max_length = NameMaxLen)
    PhoneNumber = models.CharField(max_length = PhoneNumberMaxLen)
    Email = models.EmailField()
    Address = models.CharField(max_length = AddressMaxLen)
    Birthday = models.DateField()

class User(models.Model):
    UserIDMaxLen = 20
    PasswordHashMaxLen = 50

    UserID = models.CharField(max_length = UserIDMaxLen)
    Type = models.SmallIntegerField()
    PasswordHash = models.CharField(max_length = PasswordHashMaxLen)
    Email = models.EmailField()
    
