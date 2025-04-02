from django.shortcuts import render

# Create your views here.
# core/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Attendance

@api_view(['GET'])
def get_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    return Response({
        'name': student.name,
        'finance_cleared': student.is_finance_cleared,
        'laptop_serial': student.laptop.serial_number if hasattr(student, 'laptop') else None
    })

@api_view(['POST'])
def record_attendance(request):
    student_id = request.data.get('student_id')
    student = Student.objects.get(student_id=student_id)
    Attendance.objects.create(
        student=student,
        location=request.data.get('location'),
        attendance_type=request.data.get('type')
    )
    return Response({"status": "Attendance recorded."})