from django.db import models
import os
from django.urls import reverse

def student_image_path(instance, filename):
    return f'students/{instance.student_id}/{filename}'

class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=20)
    is_finance_cleared = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=student_image_path)
    card_url = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.card_url:
            self.card_url = reverse('student-card', args=[self.student_id])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Laptop(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.serial_number

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    attendance_type = models.CharField(max_length=20, choices=[
        ('gate', 'Gate Entry'),
        ('class', 'Class Attendance'),
        ('exam', 'Exam Attendance')
    ])

    class Meta:
        ordering = ['-date', '-time']