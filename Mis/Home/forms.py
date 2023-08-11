from django import forms
   
# import GeeksModel from models.py
from api import models as api
   
# create a ModelForm
class DepartmentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Department
        fields = "__all__"

class CourseForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Course
        fields = "__all__"

class SubjectForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Subject
        fields = "__all__"

class SubjectStudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.SubjectStudent
        fields = "__all__"

class AttendanceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Attendance
        fields = "__all__"


class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Student
        fields = "__all__"


class RoutineForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Routine
        fields = "__all__"