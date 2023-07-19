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
    queryset=Student.objects.all().order_by('name')
    serializer_class=StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all().order_by('name')
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
    queryset=Semester.objects.all().order_by('name')
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


class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all().order_by('name')
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
    queryset=SubjectStudent.objects.all().order_by('subjectIns')
    serializer_class=SubjectStudentSerializer
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=Attendance.objects.all().order_by('subjectIns')
    serializer_class=AttendanceSerializer


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