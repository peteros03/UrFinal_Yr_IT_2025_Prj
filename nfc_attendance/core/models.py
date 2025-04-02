from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=50)
    is_finance_cleared = models.BooleanField(default=False)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    attendance_type = models.CharField(max_length=20)  # "gate", "exam", etc.

class Laptop(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, unique=True)