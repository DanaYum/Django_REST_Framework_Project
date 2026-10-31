from rest_framework import serializers

from students.models import Student
from employees.models import Employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"