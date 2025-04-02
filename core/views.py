from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Student, Attendance  # Correct
from core.api.serializers import StudentSerializer, AttendanceSerializer
from django.shortcuts import render
from django.db import models
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FinanceStatusForm
from .forms import StudentForm  # You'll need to create this form
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student

def is_admin(user):
    return user.is_superuser

def student_card(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'student_card.html', {'student': student})

@login_required
def admin_portal(request):
    if not request.user.is_superuser:
        return redirect('gate-portal')
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-portal')
    else:
        form = StudentForm()
    
    students = Student.objects.all()
    return render(request, 'admin_portal.html', {
        'form': form,
        'students': students
    })

@login_required
def gate_portal(request):
    return render(request, 'gate_portal.html')

@login_required
def teacher_portal(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(student_id=student_id)
            Attendance.objects.create(
                student=student,
                location="Classroom",
                attendance_type="class"
            )
        except Student.DoesNotExist:
            pass
    
    return render(request, 'teacher_portal.html')

def home(request):
    return render(request, 'core/home.html')  # You'll need to create this template

def admin_portal(request):
    return render(request, 'core/admin_portal.html')

def gate_portal(request):
    return render(request, 'core/gate_portal.html')

def teacher_portal(request):
    return render(request, 'core/teacher_portal.html')

def finance_portal(request):
    return render(request, 'core/finance_portal.html')

def student_card(request, student_id):
    from core.models import Student
    student = Student.objects.get(student_id=student_id)
    return render(request, 'core/student_card.html', {'student': student})

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import FinanceStatusForm

def finance_portal(request):
    """
    View function for the finance portal with full functionality:
    - Displays all students and their finance status
    - Allows updating finance clearance status
    - Includes search functionality
    """
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin:login')
    
    # Handle search query
    search_query = request.GET.get('search', '')
    students = Student.objects.all()
    
    if search_query:
        students = students.filter(
            models.Q(student_id__icontains=search_query) |
            models.Q(name__icontains=search_query) |
            models.Q(program__icontains=search_query)
        )
    
    # Handle status updates
    if request.method == 'POST':
        form = FinanceStatusForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            new_status = form.cleaned_data['is_finance_cleared']
            
            try:
                student = Student.objects.get(student_id=student_id)
                student.is_finance_cleared = new_status
                student.save()
                messages.success(request, f'Updated finance status for {student.name}')
            except Student.DoesNotExist:
                messages.error(request, 'Student not found')
            
            return redirect('finance-portal')
    else:
        form = FinanceStatusForm()
    
    context = {
        'students': students,
        'form': form,
        'search_query': search_query,
    }
    
    return render(request, 'core/finance_portal.html', context)


def edit_student(request, student_id):
    """
    View function to edit student information
    """
    student = get_object_or_404(Student, student_id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student {student.name} updated successfully')
            return redirect('student-card', student_id=student.student_id)
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'core/edit_student.html', {
        'form': form,
        'student': student
    })

def delete_student(request, student_id):
    """
    View function to delete a student record
    """
    student = get_object_or_404(Student, student_id=student_id)
    
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f'Student {student_name} deleted successfully')
        return redirect('home')  # Redirect to home or another appropriate page
    
    # If not POST, show confirmation page
    return render(request, 'core/confirm_delete.html', {
        'student': student
    })
