from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    custom_groups = models.ManyToManyField('auth.Group', related_name='custom_users')
    custom_permissions = models.ManyToManyField('auth.Permission', related_name='custom_permissions')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='finalProject_users',
        related_query_name='finalProject_user',
        blank=True,
        null=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='finalProject_permissions',
        related_query_name='finalProject_permission',
        blank=True,
        null= True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
class Cycle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pc(models.Model):
    numPC = models.IntegerField()
    numLapTop = models.IntegerField()

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    fingerprint = models.CharField(max_length=50)
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="students")
    class_group = models.CharField(max_length=2)

    def __str__(self):
        return str(self.user)

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff")
    image = models.CharField(max_length=1000, default='static/neologo.png')  
    description = models.CharField(max_length=1000, default='Nada.')

    def __str__(self):
        return str(self.user)

class Attendance(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE, related_name="attendances")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    check_in = models.TimeField(auto_now_add=True)
    check_out = models.TimeField(auto_now_add=True)
    pc = models.ForeignKey(Pc, on_delete=models.CASCADE, related_name="attendances")

class StaffFeedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="given_feedbacks")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="received_feedbacks")
    observation = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)

class StuFeedback(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="given_stu_feedbacks")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="received_stu_feedbacks")
    observation = models.CharField(max_length=244)
    created_at = models.DateTimeField(auto_now_add=True)
    

class PlayerScore(models.Model):
    player = models.ForeignKey('User', on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player.username}: {self.score}"