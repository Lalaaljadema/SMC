from django import forms
from django.core.exceptions import ValidationError

from .models import StudentData

class AddStudent(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'GPA']
        labels = {
        'student_number': 'Student Number', 
        'first_name': 'First Name', 
        'last_name': 'Last Name', 
        'email': 'Email', 
        'field_of_study': 'Field of Study', 
        'GPA': 'GPA'
        }
        widgets = {
        'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
        'GPA': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        student_number = cleaned_data.get('student_number')
        email = cleaned_data.get('email')
        instance = self.instance
        
        if StudentData.objects.filter(student_number=student_number).exclude(pk=instance.pk if instance else None).exists():
            self.add_error('student_number', 'Student with this student number already exists.')
            
        if StudentData.objects.filter(email=email).exclude(pk=instance.pk if instance else None).exists():
            self.add_error('email', 'Student with this email already exists.')
            
        return cleaned_data

