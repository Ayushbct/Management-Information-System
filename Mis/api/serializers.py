from rest_framework.serializers import *
from .models import *
# class YearSerializer(ModelSerializer):
#     class Meta:
#         model=Year
#         fields='__all__'

class DepartmentSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Department
        fields='__all__'

class YearSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Year
        fields='__all__'


class StudentSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Student
        fields='__all__'


class TeacherSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Teacher
        fields='__all__'

class SemesterSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Semester
        fields='__all__'

class SubjectSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Subject
        fields='__all__'

class CourseSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Course
        fields='__all__'


class SubjectStudentSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=SubjectStudent
        fields='__all__'

class AttendanceSerializer(HyperlinkedModelSerializer):
    id=ReadOnlyField()
    class Meta:
        model=Attendance
        fields='__all__'
