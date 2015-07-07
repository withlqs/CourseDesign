from django.db import models

# Create your models here.

class Student(models.Model):
    StudentID = models.CharField(max_length = 15)
    Name = models.CharField(max_length = 30)
    PhoneNumber = models.CharField(max_length = 20)
    Email = models.EmailField()
    Address = models.CharField(max_length = 100)
    Birthday = models.DateField()

class User(models.Model):
    UserID = models.CharField(max_length = 20)
    Type = models.SmallIntegerField()
    PasswordHash = models.CharField(max_length = 50)
    Email = models.EmailField()
    
