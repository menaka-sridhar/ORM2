from django.db import models
from django.contrib import admin

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=255, help_text="Staff Name")
    department = models.CharField(max_length=100, help_text="Department Name")
    doj = models.DateField(help_text="Date of Joining")

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'doj')
