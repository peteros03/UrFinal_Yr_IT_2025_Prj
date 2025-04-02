# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/students/<str:student_id>/', views.get_student),
    path('api/attendance/', views.record_attendance),
]