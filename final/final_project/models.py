from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Cycle(models.Model):
    name = models.CharField(max_length=50) 

    
    def __str__(self):
        return self.name
    
class Class(models.Model):
    group = models.CharField(max_length=3)
    time = models.CharField(max_length=50)

    
class Pc(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()

    
class Student(models.Model):
    id_stu = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=10)
    fingerprint = models.CharField(max_length=50)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="students")
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students")

    
    def __str__(self):
        return self.name

class Staff(models.Model):
    id_staff = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=10)

    
    def __str__(self):
        return self.name

class Attendance(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="cycle")
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="group")
    time = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="time")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="name")
    check_in = models.TimeField(auto_now_add=True) 
    check_out = models.TimeField(auto_now_add=True)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE, related_name="number")
    
class StaffFeedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="name")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    observation = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)

class StuFeedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="name")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    observation = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)