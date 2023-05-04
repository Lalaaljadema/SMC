from django import forms

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

        def student_data_validation(self):
            student_number = self.cleaned_data['student_number']