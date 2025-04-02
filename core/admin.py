from django.contrib import admin
from .models import Student, Laptop, Attendance
from django.utils.html import format_html

class LaptopInline(admin.StackedInline):
    model = Laptop
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'program', 'academic_year', 'photo_preview', 'is_finance_cleared')
    list_filter = ('program', 'academic_year', 'is_finance_cleared')
    search_fields = ('student_id', 'name')
    inlines = [LaptopInline]
    readonly_fields = ('photo_preview', 'card_url')
    
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "No photo"
    photo_preview.short_description = 'Preview'

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'time', 'location', 'attendance_type')
    list_filter = ('location', 'attendance_type', 'date')
    search_fields = ('student__student_id', 'student__name')