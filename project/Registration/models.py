from django.db import models

# Create your models here.
class Employeeinfo(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    country=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)