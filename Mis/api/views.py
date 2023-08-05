from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from .models import *
from .serializers import *
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