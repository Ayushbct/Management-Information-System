from django.contrib import admin
from api.models import *
# Register your models here.
admin.site.register(Year)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(SubjectStudent)
admin.site.register(Attendance)
admin.site.register(Routine)