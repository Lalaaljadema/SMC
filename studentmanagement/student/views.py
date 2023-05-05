from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

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
            form.clean()
            form.save()

            return render(request, 'student/add.html', {
            'form':form,
            'success':True})
    else:
        form = AddStudent()
    
    return render(request, 'student/add.html', {
        'form':form})

def view_student(request, id):
    return HttpResponseRedirect(reverse('index'))

def delete(request, pk):
    student = StudentData.objects.filter(pk=pk)
    if request.method == "POST":
       student.delete()

       return redirect('index')

def edit(request, pk):
    student = StudentData.objects.get(pk=pk)
    if request.method == "POST":
        form = AddStudent(request.POST, instance=student)

        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:
        form = AddStudent(instance=student)
    
    return render(request, 'student/edit.html', {
        'form':form
        })
            


