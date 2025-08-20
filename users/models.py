from django.db import models

# Create your models here.

class Department(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.CharField(max_length=255)
    courses = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Marks(models.Model):
    username = models.CharField(max_length=255)
    courses = models.CharField(max_length=255)
    marks = models.IntegerField()

    def __str__(self):
        return self.name
    

