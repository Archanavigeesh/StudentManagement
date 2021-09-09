from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=25)
    usertype=models.CharField(max_length=20)
class Student(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=50)
class State(models.Model):
    stdlogin=models.ForeignKey(Login,on_delete=models.CASCADE)
    std=models.ForeignKey(Student,on_delete=models.CASCADE)
    state=models.CharField(max_length=15)