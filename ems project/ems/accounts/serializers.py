from rest_framework import serializers
from .models import Employee, Department, Project

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary', 'designation', 'department', 'address', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    team_lead = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), required=False, allow_null=True)
    team = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True, required=False, allow_null=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'team', 'team_lead', 'status', 'start_date', 'end_date']

    
    def validate_team_lead(self, value):
        if value is None:
            return None
        return value

    def validate_team(self, value):
        if value is None:
            return []
        return value

class ProjectUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['status']

class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'salary']
