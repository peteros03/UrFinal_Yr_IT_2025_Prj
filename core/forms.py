from django import forms
from .models import Student, Laptop

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'academic_year': forms.Select(choices=[
                ('2023', '2023'),
                ('2024', '2024'),
                ('2025', '2025')
            ])
        }

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'


class FinanceStatusForm(forms.Form):
    student_id = forms.CharField(label='Student ID', max_length=20)
    is_finance_cleared = forms.BooleanField(
        label='Finance Cleared', 
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    