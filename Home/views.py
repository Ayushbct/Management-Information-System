from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib import messages
from api.serializers import * 
from rest_framework.parsers import JSONParser
# Create your views here.
def index(request):
    
    
    context={

    }
    return render(request,'index.html',context)


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})




def department(request):
    context ={}
    all_departments=Department.objects.all()
    # context['departmentform']= DepartmentForm()
    context={
        'departmentform':DepartmentForm(),
        'all_departments':all_departments,
    }
    if request.method == 'POST':
        form=DepartmentForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Department has been saved successfully')
            
        else:
            messages.error(request, 'Department cannot be saved') 
        
    return render(request, "department.html", context)

def department_delete(request,id):
    
    department=Department.objects.get(pk=id)
    department.delete()
    return redirect('/department')

def update_department(request, id):
    department = Department.objects.get(pk=id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department has been updated successfully')
            return redirect('/department')
        else:
            messages.error(request, 'Department could not be updated')

    else:
        form = DepartmentForm(instance=department)

    context = {
        'form': form,
        'department': department
    }
    return render(request, 'update_department.html', context)






@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def department_detail(request, id):
    try:
        department = Department.objects.get(pk=id)
    except Department.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Department has been created successfully')
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Department has been updated successfully')
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        department.delete()
        messages.success(request, 'Department has been deleted successfully')
        return Response(status=204)


def course(request):
    context ={}
    all_courses=Course.objects.all()
    # context['courseform']= courseForm()
    context={
        'courseform':CourseForm(),
        'all_courses':all_courses,
    }
    if request.method == 'POST':
        form=CourseForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Course has been saved successfully')
            
        else:
            messages.error(request, 'Course cannot be saved') 
        
    return render(request, "course.html", context)

def course_delete(request,id):
    
    course=Course.objects.get(pk=id)
    course.delete()
    return redirect('/course')

def update_course(request, id):
    course = Course.objects.get(pk=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course has been updated successfully')
            return redirect('/course')
        else:
            messages.error(request, 'Course could not be updated')

    else:
        form = CourseForm(instance=course)

    context = {
        'form': form,
        'course': course
    }
    return render(request, 'update_course.html', context)




def subject(request):
    context ={}
    all_subjects=Subject.objects.all()
    # context['subjectform']= subjectForm()
    context={
        'subjectform':SubjectForm(),
        'all_subjects':all_subjects,
    }
    if request.method == 'POST':
        form=SubjectForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject has been saved successfully')
            
        else:
            messages.error(request, 'Subject cannot be saved') 
        
    return render(request, "subject.html", context)

def subject_delete(request,id):
    
    subject=Subject.objects.get(pk=id)
    subject.delete()
    return redirect('/subject')

def update_subject(request, id):
    subject = Subject.objects.get(pk=id)

    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject has been updated successfully')
            return redirect('/subject')
        else:
            messages.error(request, 'Subject could not be updated')

    else:
        form = SubjectForm(instance=subject)

    context = {
        'form': form,
        'subject': subject
    }
    return render(request, 'update_subject.html', context)



def subjectstudent(request):
    context ={}
    all_subjectstudents=SubjectStudent.objects.all()
    # context['subjectstudentform']= subjectstudentForm()
    context={
        'subjectstudentform':SubjectStudentForm(),
        'all_subjectstudents':all_subjectstudents,
    }
    if request.method == 'POST':
        form=SubjectStudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Subjectstudent has been saved successfully')
            
        else:
            messages.error(request, 'Subjectstudent cannot be saved') 
        
    return render(request, "subjectstudent.html", context)

def subjectstudent_delete(request,id):
    
    subjectstudent=SubjectStudent.objects.get(pk=id)
    subjectstudent.delete()
    return redirect('/subjectstudent')

def update_subjectstudent(request, id):
    subjectstudent = SubjectStudent.objects.get(pk=id)

    if request.method == 'POST':
        form = SubjectStudentForm(request.POST, instance=subjectstudent)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subjectstudent has been updated successfully')
            return redirect('/subjectstudent')
        else:
            messages.error(request, 'Subjectstudent could not be updated')

    else:
        form = SubjectStudentForm(instance=subjectstudent)

    context = {
        'form': form,
        'subjectstudent': subjectstudent
    }
    return render(request, 'update_subjectstudent.html', context)



def attendance(request):
    context ={}
    all_attendances=Attendance.objects.all()
    # context['attendanceform']= attendanceForm()
    context={
        'attendanceform':AttendanceForm(),
        'all_attendances':all_attendances,
    }
    if request.method == 'POST':
        form=AttendanceForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance has been saved successfully')
            
        else:
            messages.error(request, 'Attendance cannot be saved') 
        
    return render(request, "attendance.html", context)

def attendance_delete(request,id):
    
    attendance=Attendance.objects.get(pk=id)
    attendance.delete()
    return redirect('/attendance')

def update_attendance(request, id):
    attendance = Attendance.objects.get(pk=id)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance has been updated successfully')
            return redirect('/attendance')
        else:
            messages.error(request, 'Attendance could not be updated')

    else:
        form = AttendanceForm(instance=attendance)

    context = {
        'form': form,
        'attendance': attendance
    }
    return render(request, 'update_attendance.html', context)

def student(request):
    context ={}
    all_students=Student.objects.all()
    # context['studentform']= studentForm()
    context={
        'studentform':StudentForm(),
        'all_students':all_students,
    }
    if request.method == 'POST':
        form=StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'student has been saved successfully')
            
        else:
            messages.error(request, 'student cannot be saved') 
        
    return render(request, "student.html", context)

def student_delete(request,id):
    
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('/student')

def update_student(request, id):
    student = Student.objects.get(pk=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'student has been updated successfully')
            return redirect('/student')
        else:
            messages.error(request, 'student could not be updated')

    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student
    }
    return render(request, 'update_student.html', context)





def routine(request):
    context ={}
    all_routines=Routine.objects.all()
    # context['routineform']= routineForm()
    context={
        'routineform':RoutineForm(),
        'all_routines':all_routines,
    }
    if request.method == 'POST':
        form=RoutineForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'routine has been saved successfully')
            
        else:
            messages.error(request, 'routine cannot be saved') 
        
    return render(request, "routine.html", context)

def routine_delete(request,id):
    
    routine=Routine.objects.get(pk=id)
    routine.delete()
    return redirect('/routine')

def update_routine(request, id):
    routine = Routine.objects.get(pk=id)

    if request.method == 'POST':
        form = RoutineForm(request.POST, instance=routine)
        if form.is_valid():
            form.save()
            messages.success(request, 'routine has been updated successfully')
            return redirect('/routine')
        else:
            messages.error(request, 'routine could not be updated')

    else:
        form = RoutineForm(instance=routine)

    context = {
        'form': form,
        'routine': routine
    }
    return render(request, 'update_routine.html', context)

