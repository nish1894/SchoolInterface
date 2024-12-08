from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically incrementing ID
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.CharField(max_length=50)
    gender = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
