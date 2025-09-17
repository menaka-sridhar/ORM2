from django.db import models
from django.contrib import admin

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255, help_text="Student Name")
    age = models.IntegerField(help_text="Age")
    dob = models.DateField(help_text="Date of Birth")

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'dob')