from django import forms
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
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
    
    class Meta:
        model = api.Routine
        fields="__all__"
        # exclude=['time_start', 'time_end']


    def clean(self):
        
        cleaned_data = super().clean()
        season = cleaned_data.get('season')
        starting_period_value = int(cleaned_data.get('starting_period_value'))
        no_of_period_value = int(cleaned_data.get('no_of_period_value'))
        time_start = cleaned_data.get('time_start')
        time_end = cleaned_data.get('time_end')
        
        day = cleaned_data.get('day')
        room_number = cleaned_data.get('room_number')


        winter_period_time = ['10:15', '11:00', '11:45', '12:30', '13:00', '13:45', '14:30', '15:15', '16:00', '16:45', '17:30']
        summer_period_time = ['10:15', '11:05', '11:55', '12:45', '13:35', '14:25', '15:15', '16:05', '16:55', '17:45', '18:35']
     
        datetime_format = "%H:%M"
        winter_period_time = [datetime.strptime(time_str, datetime_format).time() for time_str in winter_period_time]
        summer_period_time = [datetime.strptime(time_str, datetime_format).time() for time_str in summer_period_time]
        # period no        = [    '1'     ,     '2'     ,     '3'     ,     '4'     ,     '5'    ,    '6'    ,     '7'    ,     '8'    ,     '9'    ,    '10'    ,    '11'    ]
        

        if season == 'winter':
            period_time = winter_period_time
        elif season == 'summer':
            period_time = summer_period_time
        else:
            raise forms.ValidationError("Invalid season.")

        ending_period_value = starting_period_value + no_of_period_value
        # starting_period_value=1
        # ending_period_value=2
        time_start = period_time[starting_period_value - 1]
        time_end = period_time[ending_period_value - 1]

        cleaned_data['time_start'] = time_start
        cleaned_data['time_end'] = time_end
        # Check if a routine with the same room, day, and overlapping time exists
        overlapping_routines = api.Routine.objects.filter(
            room_number=room_number,
            day=day,
            time_start__lt=time_end,
            time_end__gt=time_start
        )

        if overlapping_routines.exists():
            print("room_number': 'The room is already allocated to another teacher for the same day and time.")
            raise forms.ValidationError({'room_number': 'The room is already allocated to another teacher for the same day and time.'})


        # Convert teacher names to Teacher instances
        teacher_names = self.cleaned_data.get('teacher', [])
        teacher_instances = [get_object_or_404(api.Teacher, name=teacher_name) for teacher_name in teacher_names]

        # Check if a routine with the same teacher, day, and overlapping time exists
        for teacher_instance in teacher_instances:
            overlapping_routines_teacher = api.Routine.objects.filter(
                teacher=teacher_instance,
                day=day,
                time_start__lt=time_end,
                time_end__gt=time_start
            )

            if overlapping_routines_teacher.exists():
                print(f'A routine with {teacher_instance.name}, day, and overlapping time already exists.')
                raise forms.ValidationError({'teacher': f'A routine with {teacher_instance.name}, day, and overlapping time already exists.'})    

        return cleaned_data

