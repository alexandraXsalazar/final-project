from django.contrib.auth.models import User
from django.db import models

class Cycle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pc(models.Model):
    numPC = models.IntegerField()
    numLapTop = models.IntegerField()

class Student(models.Model):
    id_stu = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=10)
    fingerprint = models.CharField(max_length=50)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="students")
    class_group = models.CharField(max_length=2)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Staff(models.Model):
    id_staff = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="attendances")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    check_in = models.TimeField(auto_now_add=True)
    check_out = models.TimeField(auto_now_add=True)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE, related_name="attendances")

class StaffFeedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="staff_feedbacks")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    observation = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)

class StuFeedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="stu_feedbacks")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    observation = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)