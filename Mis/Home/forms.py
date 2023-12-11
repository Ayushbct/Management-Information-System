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


from datetime import datetime
class RoutineForm(forms.ModelForm):
    SEASON_CHOICES = [
        ('winter', 'Winter'),
        ('summer', 'Summer')
    ]

    season = forms.TypedChoiceField(choices=SEASON_CHOICES)
    starting_period = forms.IntegerField()
    no_of_period = forms.IntegerField()
    

    class Meta:
        model = api.Routine
        fields="__all__"
        # exclude=['time_start', 'time_end']


    def clean(self):
        
        cleaned_data = super().clean()
        season = cleaned_data.get('season')
        starting_period_value = cleaned_data.get('starting_period')
        no_of_period_value = cleaned_data.get('no_of_period')
        time_start = cleaned_data.get('time_start')
        time_end = cleaned_data.get('time_end')
        
        if season not in ['winter', 'summer']:
            raise forms.ValidationError("Invalid season.")

        winter_period_time = ['10:15 a.m.', '11:00 a.m.', '11:45 a.m.', '12:30 p.m.', '1:00 p.m.', '1:45 p.m.', '2:30 p.m.', '3:15 p.m.', '4:00 p.m.', '4:15 p.m.', '5:00 p.m.']
        summer_period_time = ['10:15 a.m.', '11:05 a.m.', '11:55 a.m.', '12:45 p.m.', '1:35 p.m.','2:25 p.m.', '3:15 p.m.', '4:05 p.m.', '4:55 p.m.', '5:45 p.m.', '6:35 p.m.']
        # period no        = [    '1'     ,     '2'     ,     '3'     ,     '4'     ,     '5'    ,    '6'    ,     '7'    ,     '8'    ,     '9'    ,    '10'    ,    '11'    ]
        

        period_time = winter_period_time if season == 'winter' else summer_period_time

        # Create period_mapping dynamically using a loop
        period_mapping = {}
        for index, time in enumerate(period_time):
            period_mapping[index + 1] = time

        ending_period_value = starting_period_value + no_of_period_value

        time_start = period_mapping.get(starting_period_value)
        time_end = period_mapping.get(ending_period_value)

        cleaned_data['time_start'] = time_start
        cleaned_data['time_end'] = time_end


        return cleaned_data
