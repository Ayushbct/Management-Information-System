from django.db import models

# Create your models here.
from django.db import models
#from django.contrib.auth.models import User
from account.models import User

from datetime import date

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    file_user = models.FileField( upload_to='profile/uploaded_files/',null=True,blank=True, max_length=100)
    

    def __str__(self):
        return self.user.username

class Department(models.Model):
    name = models.CharField(max_length=250)    
    def __str__(self):
        return self.name

class Year(models.Model):

    
    year=models.CharField( max_length=50,choices=(
        ('1st Year','1st Year'),
        ('2nd Year','2nd Year'),
        ('3rd Year','3rd Year'),
        ('4th Year','4th Year'),
        ('Pass out','Pass out'),
        ),unique=True)

    def __str__(self):
        return self.year

    
class Semester(models.Model):
    name=models.CharField( max_length=50,choices=(
        ('1st Semester','1st Semester'),
        ('2nd Semester','2nd Semester'),
        ('3rd Semester','3rd Semester'),
        ('4th Semester','4th Semester'),
        ('5th Semester','5th Semester'),
        ('6th Semester','6th Semester'),
        ('7th Semester','7th Semester'),
        ('8th Semester','8th Semester'),
        ('Pass out','Pass out'),
        ),unique=True)
    year=models.ForeignKey(Year,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
# Course= BCT,BEL
class Course(models.Model): 

    name=models.CharField(max_length=100)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #year=models.ManyToManyField(Year)    
    
    def __str__(self):
        return self.name

class Student(models.Model):

    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=50,unique=True)
    
    # semester=models.ForeignKey(Semester,on_delete=models.CASCADE)
    # year=models.ForeignKey(Year,on_delete=models.CASCADE)

    def __str__(self):
        return self.name +' : '+self.roll_no



# Subject =class
class Subject(models.Model):

    name=models.CharField(max_length=100,unique=True)

    #year=models.ForeignKey(Year,on_delete=models.CASCADE)
    # semester=models.ManyToManyField(Semester)
    # student = models.ManyToManyField(Student) 
    
    def __str__(self):
        return self.name

class SubjectStudent(models.Model):
    subjectIns = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE) 

    def __str__(self):
        return self.student.roll_no

    def get_present(self):
        student =  self.student
        _class =  self.subjectIns
        try:
            present = Attendance.objects.filter(subjectIns= _class, student=student, attendance_status = 1).count()
            return present
        except:
            return 0
    
    def get_tardy(self):
        student =  self.student
        _class =  self.subjectIns
        try:
            present = Attendance.objects.filter(subjectIns= _class, student=student, attendance_status = 2).count()
            return present
        except:
            return 0

    def get_absent(self):
        student =  self.student
        _class =  self.subjectIns
        try:
            present = Attendance.objects.filter(subjectIns= _class, student=student, attendance_status = 3).count()
            return present
        except:
            return 0


class Attendance(models.Model):
    subjectIns = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    attendance_status = models.CharField(max_length=250, choices = [('1','Present'),('0.5','Late'),('0','Absent')] )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subjectIns.name + " : " +self.student.roll_no


class Teacher(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,)
    email=models.EmailField(max_length=254,unique=True,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=15,unique=True)
    post=models.CharField(max_length=40,null=True,blank=True)
    out_of_department = models.BooleanField(default=False)
    # subject=models.ManyToManyField(Subject)
    def __str__(self):
        return self.name
    




class Routine(models.Model):
    DAY_CHOICES = [
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    ]

    SESSION_CHOICES = [
        ('lecture', 'Lecture'),
        ('lab', 'Lab'),
        ('tutorial', 'Tutorial'),
        ('lecture and tutorial', 'Lecture + Tutorial'),
    ]
    SEASON_CHOICES = [
        ('winter', 'Winter'),
        ('summer', 'Summer'),
        
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    time_start = models.TimeField(blank=True,null=True)
    time_end = models.TimeField(blank=True,null=True)
    session_type = models.CharField(max_length=25, choices=SESSION_CHOICES)
    teacher = models.ManyToManyField(Teacher,blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=50,blank=True)
    season=models.CharField(max_length=10, choices=SEASON_CHOICES,default="summer")
    starting_period_value=models.CharField(max_length=10,blank=True)
    no_of_period_value=models.CharField(max_length=10,blank=True)
    year_part=models.CharField(max_length=10,blank=True)
    section=models.CharField(max_length=10,blank=True,null=True)
    note=models.CharField(max_length=10,blank=True,null=True)
    alternate_bool = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} - {self.subject} - {self.day} {self.time_start}-{self.time_end} ({self.session_type})"
