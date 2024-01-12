from rest_framework.serializers import *
from .models import *
from rest_framework import serializers
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


class TeacherSerializer(ModelSerializer):
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
    # subjectIns = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
    # student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    subjectIns = serializers.SlugRelatedField(
         queryset= Subject.objects.all(),
         slug_field='id'
     )
    student = serializers.SlugRelatedField(
         queryset= Student.objects.all(),
         slug_field='id'
     )
    # subjectIns = serializers.HyperlinkedRelatedField(
    #     queryset=Subject.objects.all(),
    #     view_name='subject-detail',
    #     lookup_field='pk',   # Use 'pk' as the lookup field instead of 'slug' or any other field
    # )
    # student = serializers.HyperlinkedRelatedField(
    #     queryset=Student.objects.all(),
    #     view_name='student-detail',
    #     lookup_field='pk',   # Use 'pk' as the lookup field instead of 'roll_no' or any other field
    # )
    class Meta:
        model=Attendance
        fields='__all__'



class RoutineSerializer(HyperlinkedModelSerializer):
    teacher = serializers.SlugRelatedField(
        many=True,
        queryset=Teacher.objects.all(),
        slug_field='name'
    )
    subject = serializers.SlugRelatedField(
        queryset=Subject.objects.all(),
        slug_field='name'
    )
    year = serializers.SlugRelatedField(
        queryset=Year.objects.all(),
        slug_field='year'
    )
    course = serializers.SlugRelatedField(
        queryset=Course.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Routine
        fields = '__all__'
        
