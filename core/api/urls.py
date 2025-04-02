from django.urls import path
from . import views
#from .api.views import StudentList, StudentDetail, AttendanceList

urlpatterns = [
    # Portal Views
    path('', views.home, name='home'),
    path('admin-portal/', views.admin_portal, name='admin-portal'),
    path('gate-portal/', views.gate_portal, name='gate-portal'),
    path('teacher-portal/', views.teacher_portal, name='teacher-portal'),
    
    # Student Views
    path('student/<str:student_id>/', views.student_card, name='student-card'),
    
    # API Endpoints
    path('api/students/', api_views.StudentList.as_view(), name='student-list'),
    path('api/students/<str:pk>/', api_views.StudentDetail.as_view(), name='student-detail'),
    path('api/attendance/', api_views.AttendanceList.as_view(), name='attendance-list'),
    path('api/verify/', api_views.VerifyStudent.as_view(), name='verify-student'),
     path('student/<str:student_id>/delete/', views.delete_student, name='delete-student'),
]