from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from .models import *
from .serializers import *
from django.db.models import Q
from datetime import datetime, timedelta
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.
# @api_view(['GET'])
# def getRoutes(Request):
#     return Response('Our Api')


# @api_view(['GET'])
# def getYears(request):
    
#     years=Year.objects.all()
#     serializer=YearSerializer(years,many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getYear(request,pk):
#     years=Year.objects.get(id =pk)
#     serializer=YearSerializer(years,many=False)
#     return Response(serializer.data)

from rest_framework import viewsets

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

class YearViewSet(viewsets.ModelViewSet):
    queryset=Year.objects.all()
    serializer_class=YearSerializer

    # This is for custom url year/id/students
    @action(detail=True,methods=['get'])
    def students(self,request,pk=None):
        try:
            year=Year.objects.get(pk=pk)
            stds=Student.objects.filter(year=year)
            stds_serializer=StudentSerializer(stds,many=True,context={'request':request})
            return Response(stds_serializer.data)
        except Exception as e:
            return Response({
                'error':'No such year found'
            })


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


    # This is for custom URL teacher/id/subjects/subject_id/students
    @action(detail=True, methods=['get'])
    def subject_students(self, request, pk=None, subject_id=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
            subject = teacher.subject.get(pk=subject_id)
            
            # students = Student.objects.filter(subjectstudent__subjectIns=subject)
            students = Student.objects.filter(subject__pk=subject_id)
            students_serializer = StudentSerializer(students, many=True, context={'request': request})
            return Response(students_serializer.data)
        except Teacher.DoesNotExist:
            return Response({'error': 'No such teacher found'})
        except Subject.DoesNotExist:
            return Response({'error': 'No such subject found'})
        

    # This is for custom URL teacher/id/subjects/subject_id/students/student_id/
    @action(detail=True, methods=['get'])
    def subject_student(self, request, pk=None, subject_id=None, student_id=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
            subject = teacher.subject.get(pk=subject_id)
            student = Student.objects.get(pk=student_id)

            student_serializer = StudentSerializer(student, context={'request': request})

            
            return Response(student_serializer.data)

        except Teacher.DoesNotExist:
            return Response({'error': 'No such teacher found'})
        except Subject.DoesNotExist:
            return Response({'error': 'No such subject found'})
        except Student.DoesNotExist:
            return Response({'error': 'No such student found'})


class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    # This is for custom URL teacher/id/subjects
    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
            subjects = teacher.subject.all()
            subjects_serializer = SubjectSerializer(subjects, many=True, context={'request': request})
            return Response(subjects_serializer.data)
        except Teacher.DoesNotExist:
            return Response({'error': 'No such teacher found'})
        


class SemesterViewSet(viewsets.ModelViewSet):
    queryset=Semester.objects.all()
    serializer_class=SemesterSerializer
    # This is for custom URL semester/id/students
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        try:
            semester = Semester.objects.get(pk=pk)
            students = Student.objects.filter(semester=semester)
            students_serializer = StudentSerializer(students, many=True, context={'request': request})
            return Response(students_serializer.data)
        except Semester.DoesNotExist:
            return Response({'error': 'No such semester found'})

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # This is for custom url subject/id/students
    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        try:
            subject = Subject.objects.get(pk=pk)
            semesters = subject.semester.all()
            students = Student.objects.filter(semester__in=semesters)
            students_serializer = StudentSerializer(students, many=True, context={'request': request})
            
            return Response(students_serializer.data)
        except Subject.DoesNotExist:
            return Response({'error': 'No such subject found'})


    # This is for custom URL teacher/id/subjects/subject_id
    @action(detail=True, methods=['get'])
    def subject(self, request, pk=None, subject_id=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
            subject = teacher.subject.get(pk=subject_id)  # This line is updated
            subject_serializer = SubjectSerializer(subject, context={'request': request})
            return Response(subject_serializer.data)
        except Teacher.DoesNotExist:
            return Response({'error': 'No such teacher found'})
        except Subject.DoesNotExist:
            return Response({'error': 'No such subject found'})


class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

    # Custom URL course/id/years
    @action(detail=True, methods=['get'])
    def years(self, request, pk=None):
        try:
            program = Course.objects.get(pk=pk)
            years = Course.year.all()
            years_serializer = YearSerializer(years, many=True, context={'request': request})
            return Response(years_serializer.data)
        except Course.DoesNotExist:
            return Response({'error': 'No such program found'})
    
    # Custom URL program/id/subjects
    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        try:
            program = Course.objects.get(pk=pk)
            subjects = Course.subject.all()
            subjects_serializer = SubjectSerializer(subjects, many=True, context={'request': request})
            return Response(subjects_serializer.data)
        except Course.DoesNotExist:
            return Response({'error': 'No such program found'})

class SubjectStudentViewSet(viewsets.ModelViewSet):
    queryset=SubjectStudent.objects.all()
    serializer_class=SubjectStudentSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

    # This is for custom URL teacher/id/subjects/subject_id/students/student_id/attendance/
    @action(detail=True, methods=['get'])
    def get_student_attendance(self, request, pk=None, subject_id=None, student_id=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
            subject = teacher.subject.get(pk=subject_id)
            student = Student.objects.get(pk=student_id)

            attendance_records = Attendance.objects.filter(subjectIns=subject, student=student)
            attendance_serializer = AttendanceSerializer(attendance_records, many=True, context={'request': request})
            return Response(attendance_serializer.data)

        except Teacher.DoesNotExist:
            return Response({'error': 'No such teacher found'})
        except Subject.DoesNotExist:
            return Response({'error': 'No such subject found'})
        except Student.DoesNotExist:
            return Response({'error': 'No such student found'})

    # This is for custom URL teacher/id/subjects/subject_id/students/student_id/attendance/
    @action(detail=True, methods=['post'])
    def create_student_attendance(self, request, pk=None, subject_id=None, student_id=None):
        try:
            teacher = Teacher.objects.get(pk=pk)
            subject = teacher.subject.get(pk=subject_id)
            student = Student.objects.get(pk=student_id)

            attendance_data = {
                'subjectIns': subject.id,
                'student': student.id,
                'attendance_date': request.data.get('attendance_date'),
                'attendance_status': request.data.get('attendance_status', '1'),  # Default attendance_status to 'Present' if not provided
            }
            attendance_serializer = AttendanceSerializer(data=attendance_data,many=False, context={'request': request})
            if attendance_serializer.is_valid():
                attendance_serializer.save()
                return redirect('/api'+'/teachers/'+str(teacher.pk)+'/subjects/'+str(subject.pk)+'/students/'+str(student.pk)+'/attendance')
                # return Response(attendance_serializer.data)
            else:
                return Response(attendance_serializer.errors)

        except Teacher.DoesNotExist:
            return Response({'error': 'No such teacher found'})
        except Subject.DoesNotExist:
            return Response({'error': 'No such subject found'})
        except Student.DoesNotExist:
            return Response({'error': 'No such student found'})



class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    # def create(self, request, *args, **kwargs):
    #     winter_period_time = ['10:15', '11:00', '11:45', '12:30', '13:00', '13:45', '14:30', '15:15', '16:00', '16:45', '17:30']
    #     summer_period_time = ['10:15', '11:05', '11:55', '12:45', '13:35', '14:25', '15:15', '16:05', '16:55', '17:45', '18:35']
     
    #     datetime_format = "%H:%M"
    #     winter_period_time = [datetime.strptime(time_str, datetime_format).time() for time_str in winter_period_time]
    #     summer_period_time = [datetime.strptime(time_str, datetime_format).time() for time_str in summer_period_time]

    #     # teacher_id = request.data.get('teacher')
    #     teacher_names=request.POST.getlist('teacher')
    #     room_number = request.data.get('room_number')
    #     day = request.data.get('day')

    #     season = request.data.get('season')
    #     starting_period_value = int(request.data.get('starting_period_value', 0))
    #     no_of_period_value = int(request.data.get('no_of_period_value', 0))

    #     if season == 'winter':
    #         period_time = winter_period_time
    #     elif season == 'summer':
    #         period_time = summer_period_time
    #     else:
    #         return Response({'error': 'Invalid season.'}, status=status.HTTP_400_BAD_REQUEST)

    #     if starting_period_value < 0 or starting_period_value >= len(period_time):
    #         return Response({'error': 'Invalid starting period value.'}, status=status.HTTP_400_BAD_REQUEST)

    #     ending_period_value = starting_period_value + no_of_period_value
    #     if ending_period_value < 0 or ending_period_value >= len(period_time):
    #         return Response({'error': 'Invalid ending period value.'}, status=status.HTTP_400_BAD_REQUEST)

    #     time_start = period_time[starting_period_value - 1]
    #     time_end = period_time[ending_period_value - 1]

    #     # Create a mutable copy of request.data
    #     data_copy = request.data.copy()
    #     data_copy['time_start'] = time_start
    #     data_copy['time_end'] = time_end

    #     # print(request.data)
    #     # teacher_data_list = request.data.getlist('teacher', [])
    #     # print(teacher_data_list)

    #     overlapping_routines = Routine.objects.none()
    #     # Check if a routine with the same room, day, and overlapping time exists
    #     overlapping_routines = Routine.objects.filter(
    #         room_number=room_number,
    #         day=day,
    #         time_start__lt=time_end,
    #         time_end__gt=time_start
    #     )

        
        

        
    #     teacher_names=request.POST.getlist('teacher')
    #     # print(teacher_names)
    #     # teacher_names = request.data.get('teacher', [])
    #     # print(teacher_names)

    #     # Convert teacher names to Teacher instances or IDs
    #     teacher_instances = []
    #     for teacher_name in teacher_names:
    #         teacher_instance = get_object_or_404(Teacher, name=teacher_name)
    #         teacher_instances.append(teacher_instance)

    #     overlapping_routines_teacher = Routine.objects.none()
    #     # Check if a routine with the same teacher, day, and overlapping time exists
    #     for teacher_instance in teacher_instances:
    #         overlapping_routines_teacher = Routine.objects.filter(
    #             teacher=teacher_instance,
    #             day=day,
    #             time_start__lt=time_end,
    #             time_end__gt=time_start
    #         )

        

    #     if overlapping_routines_teacher.exists():
    #         return Response(
    #             {'error':'A routine with the same teacher, day, and overlapping time already exists.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
        
    #     elif overlapping_routines.exists():
    #         return Response(
    #             {
    #                 'error': 'The room is already allocated to another teacher for the same day and time.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
        
    #     else:
    #         serializer = self.get_serializer(data=data_copy)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)

    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def create(self, request, *args, **kwargs):
        teacher_names,season, starting_period_value, no_of_period_value, room_number, day = self.initialize_and_validate_input(request)
        period_time = self.get_period_time(season)
        time_start, time_end = self.calculate_time_range(period_time, starting_period_value, no_of_period_value)
        data_copy = self.update_request_data(request.data, time_start, time_end)

        overlapping_routines_teacher = self.check_overlapping_routines_teacher(data_copy, day, time_start, time_end,teacher_names,room_number)
        overlapping_routines=self.check_overlapping_routines(room_number, day, time_start, time_end,teacher_names)
        # print(overlapping_routines_teacher)
        # print(overlapping_routines)
        if overlapping_routines_teacher.exists():
            return Response(
                {'error': 'A routine with the same teacher, day, and overlapping time already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif overlapping_routines.exists():
            return Response(
                {'error': 'The room is already allocated to another teacher for the same day and time.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
        # indentation
            serializer = self.get_serializer(data=data_copy)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)

    #     # Use the existing functions to initialize and validate input
    #     teacher_names, season, starting_period_value, no_of_period_value, room_number, day = self.initialize_and_validate_input(request)

    #     # Use the existing functions to get period time and calculate time range
    #     period_time = self.get_period_time(season)
    #     time_start, time_end = self.calculate_time_range(period_time, starting_period_value, no_of_period_value)
        

    #     # Use the existing functions to check overlapping routines
    #     overlapping_routines = self.check_overlapping_routines(room_number, day, time_start, time_end, teacher_names, instance.id)
    #     overlapping_routines_teacher = self.check_overlapping_routines_teacher(request.data, day, time_start, time_end, teacher_names, room_number, instance.id)

    #     # Return an error response if there are overlapping routines
    #     if overlapping_routines.exists():
    #         return Response(
    #             {'error': 'Updating the routine would cause an overlap with another routine.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #     elif overlapping_routines_teacher.exists():
    #         return Response(
    #             {'error': 'Updating the routine would cause an overlap with another routine for the same teacher.'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )

    #     # Perform the update if there are no overlapping routines
    #     self.perform_update(serializer)
    #     return Response(serializer.data)



    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        teacher_names, season, starting_period_value, no_of_period_value, room_number, day = self.initialize_and_validate_input(request)
        period_time = self.get_period_time(season)
        time_start, time_end = self.calculate_time_range(period_time, starting_period_value, no_of_period_value)
        data_copy = self.update_request_data(request.data, time_start, time_end)

        overlapping_routines_teacher = self.check_overlapping_routines_teacher(data_copy, day, time_start, time_end, teacher_names, room_number)
        overlapping_routines = self.check_overlapping_routines(room_number, day, time_start, time_end, teacher_names)

        if overlapping_routines_teacher.exists() and not overlapping_routines_teacher.filter(pk=instance.pk).exists():
            return Response(
                {'error': 'A routine with the same teacher, day, and overlapping time already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif overlapping_routines.exists() and not overlapping_routines.filter(pk=instance.pk).exists():
            return Response(
                {'error': 'The room is already allocated to another teacher for the same day and time.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            serializer = self.get_serializer(instance, data=data_copy)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

        return Response(serializer.data)

    
    def initialize_and_validate_input(self, request):
        # Add input validation logic here
        # For simplicity, assuming the input is valid
        # teacher_names = request.data.getlist('teacher')
        teacher_names=request.data.get('teacher')
        # print(teacher_names)
        room_number = request.data.get('room_number')
        day = request.data.get('day')
        season = request.data.get('season')
        starting_period_value = int(request.data.get('starting_period_value', 0))
        no_of_period_value = int(request.data.get('no_of_period_value', 0))

        return teacher_names,season, starting_period_value, no_of_period_value, room_number, day

    def get_period_time(self, season):
        winter_period_time = ['10:15', '11:00', '11:45', '12:30', '13:00', '13:45', '14:30', '15:15', '16:00', '16:45', '17:30']
        summer_period_time = ['10:15', '11:05', '11:55', '12:45', '13:35', '14:25', '15:15', '16:05', '16:55', '17:45', '18:35']

        return winter_period_time if season == 'winter' else summer_period_time

    def calculate_time_range(self, period_time, starting_period_value, no_of_period_value):
        time_start = period_time[starting_period_value - 1]
        time_end = period_time[starting_period_value + no_of_period_value - 1]
        return time_start, time_end

    def update_request_data(self, data, time_start, time_end):
        data_copy = data.copy()
        data_copy['time_start'] = time_start
        data_copy['time_end'] = time_end
        # print(data_copy)
        return data_copy

    def check_overlapping_routines(self, room_number, day, time_start, time_end,teacher_names, current_routine_id=None):
        query = Routine.objects.filter(
            room_number=room_number,
            day=day,
            time_start__lt=time_end,
            time_end__gt=time_start
        )

        if current_routine_id:
            query = query.exclude(id=current_routine_id)

        return query

    def check_overlapping_routines_teacher(self, data, day, time_start, time_end, teacher_names, room_number, current_routine_id=None):
        # print(teacher_names)
        teacher_instances = Teacher.objects.filter(name__in=teacher_names)
        # print("fjsdj")
        # print(teacher_instances)
        

        overlapping_routines_teacher = Routine.objects.none()   

        for teacher_instance in teacher_instances:
            # print(teacher_instance)
            # Check for overlapping routines in terms of time and room_number
            query = Routine.objects.filter(
                teacher=teacher_instance,
                day=day,
                time_start__lt=time_end,
                time_end__gt=time_start,
                
            )
            # print("hello")
            # print(query)

            # Exclude the routine with the given current_routine_id (if provided)
            if current_routine_id:
                query = query.exclude(id=current_routine_id)    

            # Union the query with the existing overlapping_routines_teacher queryset
            overlapping_routines_teacher = overlapping_routines_teacher.union(query)    
            

        return overlapping_routines_teacher




    # For example: /api/routines/get_routines_by_teacher_and_room/?teacher_id=1&room_number=101
    @action(detail=False, methods=['GET'])
    def get_routines_by_teacher_and_room(self, request):
        teacher_id = request.query_params.get('teacher_id')
        room_number = request.query_params.get('room_number')

        routines = Routine.objects.filter(
            teacher_id=teacher_id,
            room_number=room_number
        )

        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_routines_by_Year_and_section(self, request):
        year_id = request.query_params.get('year_id')
        year_part = request.query_params.get('year_part')
        section= request.query_params.get('section')

        routines = Routine.objects.filter(
           year_id=year_id,
           year_part=year_part,
           section=section
        )

        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)
    # For example: /api/routines/get_routines_by_teacher/?teacher_id=1
    @action(detail=False, methods=['GET'])
    def get_routines_by_teacher(self, request):
        teacher_id = request.query_params.get('teacher_id')

        routines = Routine.objects.filter(
            teacher=teacher_id
        )

        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)


    # For example: /api/routines/get_routines_by_room/?room_number=101
    @action(detail=False, methods=['GET'])
    def get_routines_by_room(self, request):
        room_number = request.query_params.get('room_number')

        routines = Routine.objects.filter(
            room_number=room_number
        )

        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)
    
    # For example: /api/routines/get_routines_by_course_and_year/?course_id=3&year=4
    @action(detail=False, methods=['GET'])
    def get_routines_by_course_and_year_section_part(self, request):
        course_id = request.query_params.get('course_id')
        year = request.query_params.get('year')
        year_part = request.query_params.get('year_part')
        section= request.query_params.get('section')

        routines = Routine.objects.filter(
            course_id=course_id,
            year=year,
            year_part=year_part,
            section=section,

        )

        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_routines_by_course_and_year(self, request):
        course_id = request.query_params.get('course_id')
        year = request.query_params.get('year')
        routines = Routine.objects.filter(
            course_id=course_id,
            year=year,
        )

        serializer = self.get_serializer(routines, many=True)
        return Response(serializer.data)




def Deletedepartments(request):
    years=Department.objects.all().delete()
    return redirect('/api')

def Deleteyears(request):
    years=Year.objects.all().delete()
    return redirect('/api')
def Deletestudents(request):
    year=Student.objects.all().delete()
    return redirect('/api')
def Deleteteachers(request):
    years=Teacher.objects.all().delete()
    return redirect('/api')
def Deletesemesters(request):
    years=Semester.objects.all().delete()
    return redirect('/api')
def Deletesubjects(request):
    years=Subject.objects.all().delete()
    return redirect('/api')

def Deletecourses(request):
    years=Course.objects.all().delete()
    return redirect('/api')

def Deletesubjectstudents(request):
    years=SubjectStudent.objects.all().delete()
    return redirect('/api')

def Deleteattendances(request):
    years=Attendance.objects.all().delete()
    return redirect('/api')