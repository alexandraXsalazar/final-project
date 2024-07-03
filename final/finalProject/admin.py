from django.contrib import admin
from .models import User, Cycle, Pc, Student, Staff, Attendance, StaffFeedback, StuFeedback, Comment, Post,Like, Follow
# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(StuFeedback)
admin.site.register(Cycle)
admin.site.register(Pc)
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(StaffFeedback)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Like)