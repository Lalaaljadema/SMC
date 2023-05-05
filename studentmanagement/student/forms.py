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
        'student_number': forms.NumberInput(attrs={'class': 'form-control block py-2.5  px-0 w-[400px] text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-800 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600'}), 
        'first_name': forms.TextInput(attrs={'class': 'form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-800 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-800 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600'}),
        'email': forms.EmailInput(attrs={'class': 'form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-800 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600'}),
        'field_of_study': forms.TextInput(attrs={'class': 'form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-800 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600'}),
        'GPA': forms.NumberInput(attrs={'class': 'form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-800 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600'}),
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

