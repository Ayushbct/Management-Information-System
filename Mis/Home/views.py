from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib import messages
from api.serializers import * 
from rest_framework.parsers import JSONParser

from api.models import *
import os
import pandas as pd
from django_pandas.io import read_frame
# Create your views here.
def index(request):
    # uploaded_file_url=''
    # if request.method == "POST":
        
    #     uploaded_file=request.FILES['fileRoutine']
    #     fs=FileSystemStorage()
    #     if fs.exists(uploaded_file.name):
    #         messages.info(request, 'File already exists in folder')
    #         fs.delete(uploaded_file.name)
        
    #     name = fs.save(uploaded_file.name,uploaded_file)
    #     uploaded_file_url = fs.url(name)
    #     messages.success(request, 'File is now uploaded not to database')
    # context = {
    #     'uploaded_file_url': uploaded_file_url,
    # }
    file_path=''
    
    if request.method == 'POST':
        profile=Profile.objects.get(user=request.user)
        if profile.file_user:
            file_path=profile.file_user.path
            if os.path.exists(file_path):
                os.remove(file_path)

        profile.file_user=request.FILES['fileRoutine']
        profile.save()
        messages.success(request, 'File added to database')
        if profile.file_user:
            uploaded_file_url = profile.file_user.url
            excel_file = uploaded_file_url
            print(excel_file)
            
            if os.path.exists(profile.file_user.path):
                excel_file = profile.file_user.path
                
            
        
    #         empexceldata = pd.read_excel(excel_file)
            
    #         dbframe = empexceldata
    #         dbframe.Email=dbframe.Email.fillna("-")
    #         for dbframe in dbframe.itertuples():
    #             # print(dbframe.Phone)
    #             if Newapp.objects.filter(newappphone=dbframe.Phone).exists()==False:
    #                 if len(dbframe.Name)>0:
    #                     newapp=Newapp.objects.create(profile=profile,newappname=dbframe.Name,newappemail=dbframe.Email, newappphone=dbframe.Phone,newappaddress=dbframe.Address,newappdepart=dbframe.Department,newappposition=dbframe.Position)
    #                     newapp.save()                
            

    # profile=Profile.objects.get(user=request.user)
    # newapp_data = Newapp.objects.filter(profile=profile).values_list("newappname","newappemail","newappphone","newappaddress","newappdepart","newappposition")
    
    # data = pd.DataFrame(list(newapp_data),columns=["Name","Email","Phone","Address","Department","Position"])
    # data.set_index('Name', inplace=True)
    
    # newpath="media/"+'Invigilators List-'+profile.user.username+'.xlsx'
    # data.to_excel(newpath)    
    # path = Path(newpath)
    # if profile.file_generated:
    #     if os.path.exists(profile.file_generated.path):
    #         os.remove(profile.file_generated.path)
    # with path.open(mode='rb') as f:
    #     profile.file_generated = File(f, name=path.name)
        
    #     profile.save()

    # file_path=path
    # if os.path.exists(file_path):
    #     os.remove(file_path)


    
    # file_generated_basename=''
    
    
    
    # if profile.file_generated:
    #     file_generated_basename=os.path.basename(profile.file_generated.path)
    # # Upload files code above below new app
    # profile=Profile.objects.get(user=request.user)
    # newapp_data=Newapp.objects.filter(profile=profile)
    # departments=[]
    # positions=[]
    # deparment_numbers=[]
    # position_numbers=[]
    # for nap in newapp_data:
    #     departments.append(nap.newappdepart)
    #     positions.append(nap.newappposition)
    # department_removing_dup=[*set(departments)]
    # position_removing_dup=[*set(positions)]
    # remove=['nan','-']
    # for r in remove:
    #     if r in department_removing_dup:
    #         department_removing_dup.remove(r)
    #     if r in position_removing_dup:
    #         position_removing_dup.remove(r)
    # for drd in department_removing_dup:
    #     deparment_numbers.append(departments.count(drd))
    # for prd in position_removing_dup:
    #     position_numbers.append(positions.count(prd))
    
    # # print(department_removing_dup)
    context={
        
        
        
        
    }
    
    context={

    }
    return render(request,'index.html',context)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout

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
            # print(form.cleaned_data)
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

def teacher(request):
    
    context ={}
    all_teachers=Teacher.objects.all()
    # context['routineform']= routineForm()
    context={
        'teacherform':TeacherForm(),
        'all_teachers':all_teachers,
    }
    if request.method == 'POST':
        form=TeacherForm(request.POST)
        
        if form.is_valid():    
            # print(form.cleaned_data)
            form.save()
            messages.success(request, 'Teacher has been saved successfully')
            
        else:
            messages.error(request, 'Teacher cannot be saved') 
        
    return render(request, "teacher.html", context)
def teacher_delete(request,id):
    
    teacher=Teacher.objects.get(pk=id)
    # teacher.profile.user
    user=User.objects.get(username=teacher.phone)
    user.delete()
    messages.success(request, 'Teacher deleted successfully')
    return redirect('/teacher')

def update_teacher(request, id):
    teacher = Teacher.objects.get(pk=id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'teacher has been updated successfully')
            return redirect('/teacher')
        else:
            messages.error(request, 'teacher could not be updated')

    else:
        form = TeacherForm(instance=teacher)

    context = {
        'form': form,
        'teacher': teacher
    }
    return render(request, 'update_teacher.html', context)

def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword1=request.POST['loginpassword1']
        
        user=authenticate(username=loginusername,password=loginpassword1)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged in')
            return redirect('/')
        else:
            messages.error(request, 'Unsuccessfull to log in, Please try again')
            return redirect('/')
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')


def change_password(request):
    if request.method=="POST":
        change_password1=request.POST['change_password1']
        change_password2=request.POST['change_password2']
        # print(change_password1)
        if change_password1!=change_password2:
            messages.error(request,"Passwords do not match try again")
            return redirect('/')
        u = request.user
        u.set_password(change_password1)
        u.save()
        messages.success(request, 'Successfully password changed')
    return redirect('/')