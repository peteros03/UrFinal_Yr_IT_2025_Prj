from django.urls import path
from . import views
from .api import views as api_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Portal Views
    path('', views.home, name='home'),
    path('admin-portal/', views.admin_portal, name='admin-portal'),
    path('gate-portal/', views.gate_portal, name='gate-portal'),
    path('teacher-portal/', views.teacher_portal, name='teacher-portal'),
    path('finance-portal/', views.finance_portal, name='finance-portal'),
    
    # Student Views
    path('student/<str:student_id>/', views.student_card, name='student-card'),
    path('student/<str:student_id>/edit/', views.edit_student, name='edit-student'),
    path('student/<str:student_id>/delete/', views.delete_student, name='delete-student'),
    
    # Attendance Views
    path('attendance/', views.attendance_list, name='attendance-list'),
    path('attendance/<int:pk>/delete/', views.delete_attendance, name='delete-attendance'),
    
    # NFC Operations
    path('nfc/write/', views.nfc_write, name='nfc-write'),
    path('nfc/read/', views.nfc_read, name='nfc-read'),

    path('finance-portal/', login_required(views.finance_portal), name='finance-portal'),

    path('student/<str:student_id>/edit/', views.edit_student, name='edit-student'),
]

# Create api/urls.py for API endpoints
api_urlpatterns = [
    path('students/', api_views.StudentList.as_view()),
    path('students/<str:pk>/', api_views.StudentDetail.as_view()),
    path('attendance/', api_views.AttendanceList.as_view()),
]



