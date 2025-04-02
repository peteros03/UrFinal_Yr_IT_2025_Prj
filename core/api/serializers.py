from rest_framework import serializers
from core.models import Student, Attendance, Laptop

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['serial_number']

class StudentSerializer(serializers.ModelSerializer):
    laptop = LaptopSerializer(read_only=True)
    photo_url = serializers.SerializerMethodField()
    card_url = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
    
    def get_photo_url(self, obj):
        if obj.photo:
            return self.context['request'].build_absolute_uri(obj.photo.url)
        return None
    
    def get_card_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.card_url)

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    student_id = serializers.CharField(source='student.student_id', read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'