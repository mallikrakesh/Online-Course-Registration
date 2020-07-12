from django.db import models

class CourseModel(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,unique=True,default=None)
    faculty=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    fee=models.FloatField()
    duration=models.IntegerField()

class StudentModel(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

class EnrollModel(models.Model):
    eid=models.AutoField(primary_key=True)
    cid=models.IntegerField()
    contact=models.IntegerField()