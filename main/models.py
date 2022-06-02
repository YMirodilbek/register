from django.db import models

# Create your models here.

class Jobs(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee1(models.Model):
    job=models.ForeignKey(Jobs,on_delete=models.SET_NULL,null=True,blank=True, related_name="second_first")
    full_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    phone= models.CharField(max_length=11)

    def __str__(self):
        return self.job.name


class BaseJob(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class BaseEmployee(models.Model):
    STATUS=(
        ("Junior","Junior"),
        ("Middle","Middle"),
        ("Senior","Senior"),
        ("TeamLead","TeamLead"),

    )
    full_name = models.CharField(max_length=100)
    job = models.ForeignKey(BaseJob,on_delete=models.SET_NULL,null=True,related_name='first_second') 
    degree =  models.CharField(choices=STATUS,max_length=50,default="Junior")
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.full_name


class Register(models.Model):
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=8,unique=True)
    first_name = models.CharField(max_length=80)
    last_name=  models.CharField(max_length=100)
    def __str__(self):
        return self.username
    



    
