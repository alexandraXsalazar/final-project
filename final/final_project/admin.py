from django.contrib import admin
from .models import Cycle, Pc, Student, Staff, Attendance, StaffFeedback, StuFeedback
# Register your models here.
admin.site.register(Student)
admin.site.register(StuFeedback)
admin.site.register(Cycle)
admin.site.register(Pc)
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(StaffFeedback)

