#-*- coding: UTF-8 -*- 
from django.db import models
from StuInfo import *

# Create your models here.

class Student(models.Model):
    StudentIDMaxLen = 15
    NameMaxLen = 30
    PhoneNumberMaxLen = 20
    AddressMaxLen = 100

    StudentID = models.CharField(unique = True, null = False, max_length = StudentIDMaxLen)
    Name = models.CharField(null = False, max_length = NameMaxLen)
    PhoneNumber = models.CharField(max_length = PhoneNumberMaxLen)
    Email = models.EmailField()
    Address = models.CharField(max_length = AddressMaxLen)
    Birthday = models.DateField(null = False)

class User(models.Model):
    UserIDMaxLen = 20
    PasswordHashMaxLen = 50

    UserID = models.CharField(unique = True, null = False, max_length = UserIDMaxLen)
    Type = models.SmallIntegerField(null = False)
    PasswordHash = models.CharField(null = False, max_length = PasswordHashMaxLen)
    Email = models.EmailField()

