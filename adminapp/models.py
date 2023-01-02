from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Gender=models.CharField(max_length=10,null=True,blank=True)
    Image=models.ImageField(upload_to="student",null=True,blank=True)
    City=models.CharField(max_length=100,null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)

class Admin(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="student", null=True, blank=True)
    Username = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)
    CPassword = models.CharField(max_length=100)

class Category(models.Model):
    CName = models.CharField(max_length=100, null=True, blank=True)
    CDesc = models.CharField(max_length=100, null=True, blank=True)
    CImage = models.ImageField(upload_to="category", null=True, blank=True)

class Product(models.Model):
    Cat=models.CharField(max_length=100, null=True, blank=True)
    Pro=models.CharField(max_length=100, null=True, blank=True)

    Price=models.IntegerField(null=True, blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    Desc=models.CharField(max_length=100, null=True, blank=True)
    Image=models.ImageField(upload_to="product", null=True, blank=True)
