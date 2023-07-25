from django.db import models

# Create your models here.

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
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year=models.ManyToManyField(Year)    
    
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

    year=models.ForeignKey(Year,on_delete=models.CASCADE)
    semester=models.ManyToManyField(Semester)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE) 
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
            present = Attendance.objects.filter(subjectIns= _class, student=student, type = 1).count()
            return present
        except:
            return 0
    
    def get_tardy(self):
        student =  self.student
        _class =  self.subjectIns
        try:
            present = Attendance.objects.filter(subjectIns= _class, student=student, type = 2).count()
            return present
        except:
            return 0

    def get_absent(self):
        student =  self.student
        _class =  self.subjectIns
        try:
            present = Attendance.objects.filter(subjectIns= _class, student=student, type = 3).count()
            return present
        except:
            return 0


class Attendance(models.Model):
    subjectIns = models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    type = models.CharField(max_length=250, choices = [('1','Present'),('0.5','Late'),('0','Absent')] )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subjectIns.name + " : " +self.student.roll_no


class Teacher(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,unique=True)
    subject=models.ManyToManyField(Subject)
    def __str__(self):
        return self.name
    



