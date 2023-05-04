from django.shortcuts import render, redirect

from .models import StudentData
from .forms import AddStudent

def index(request):
    students = StudentData.objects.all()
    return render(request, 'student/index.html', {
        'students':students
        })

def add_student(request):
    if request.method == "POST":
        form = AddStudent(request.POST)

        if form.is_valid():
            form.save()

        return redirect('index')
    else:
        form = AddStudent()
    
    return render(request, 'student/add.html', {
        'form':form})

def delete(request, pk):
    student = StudentData.objects.filter(pk=pk)
    if request.method == "POST":
       student.delete()

       return redirect('index')


