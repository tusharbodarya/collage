from rest_framework import serializers
from main.models import Department,Subject,StudentID,Student,SubjectMarks

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields="__all__"

class StudentIdSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentID
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
        
class SubjectMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectMarks
        fields="__all__"