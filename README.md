# Ex02 Django ORM Web Application
## Date: 18.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
model.py
from django.db import models
from django.contrib import admin
# Create your models here.

class StudentDetail(models.Model):
        name = models.CharField(max_length=250, help_text="Enter the studnt name")
        age = models.IntegerField(help_text="Enter the age between 18 to 22")
        dob = models.DateField(help_text="Enter the Date of Birth")
        reg_no = models.IntegerField(help_text="Enter the Register Number")
        
class StudentDetailsAdmin(admin.ModelAdmin):
        list_display = ('name', 'age', 'dob', 'reg_no')


admin.py
from django.contrib import admin
from.models import StudentDetail, StudentDetailsAdmin

# Register your models here.

admin.site.register(StudentDetail, StudentDetailsAdmin)

```
## OUTPUT
![alt text](<Screenshot 2025-09-18 135205.png>)
![alt text](<Screenshot 2025-09-18 135219.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
