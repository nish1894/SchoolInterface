from django.shortcuts import render
from .models import Student, Teacher, Classroom


def home(request):
    return render(request, 'school/home.html')


def students(request):
    students = Student.objects.all()
    return render(request, 'school/students.html', {'students': students})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teachers.html', {'teachers': teachers})


def classrooms(request):
    classrooms = Classroom.objects.all()
    return render(request, 'school/classrooms.html', {'classrooms': classrooms})
