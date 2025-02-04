from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from rest_framework.decorators import api_view


from .models import Employee, Department, Project
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer, ProjectUpdateStatusSerializer, EmployeeSalarySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['get'])
    def department(self, request, pk=None):
        employee = self.get_object()
        return Response(DepartmentSerializer(employee.department).data)

    @action(detail=False, methods=['get'])
    def highest_salary(self, request):
        highest_salary_employee = Employee.objects.order_by('-salary').first()
        return Response(EmployeeSalarySerializer(highest_salary_employee).data)

    @action(detail=False, methods=['get'])
    def second_highest_salary(self, request):
        second_highest_salary_employee = Employee.objects.order_by('-salary')[1:2]
        return Response(EmployeeSalarySerializer(second_highest_salary_employee, many=True).data)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def retrieve(self, request, *args, **kwargs):
        department = self.get_object()
        employees = Employee.objects.filter(department=department)
        department_data = DepartmentSerializer(department).data
        department_data['employees'] = EmployeeSerializer(employees, many=True).data
        return Response(department_data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['put'])
    def add_member(self, request, pk=None):
        project = self.get_object()
        employee_id = request.data.get('employee_id')
        try:
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        project.team.add(employee)
        return Response(ProjectSerializer(project).data)

   
    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        project = self.get_object()
        serializer = ProjectUpdateStatusSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get total salary of employees under each department
@api_view(['GET'])
def total_salary_per_department(request):
    departments = Department.objects.all()
    result = {}
    for department in departments:
        total_salary = Employee.objects.filter(department=department).aggregate(Sum('salary'))['salary__sum']
        result[department.name] = total_salary
    return Response(result)

# Get all NEW projects
@api_view(['GET'])
def get_new_projects(request):
    projects = Project.objects.filter(status='NEW')
    return Response(ProjectSerializer(projects, many=True).data)

# Get all ON-GOING projects
@api_view(['GET'])
def get_ongoing_projects(request):
    projects = Project.objects.filter(status='ON-GOING')
    return Response(ProjectSerializer(projects, many=True).data)

# Get all ENDED projects
@api_view(['GET'])
def get_ended_projects(request):
    projects = Project.objects.filter(status='ENDED')
    return Response(ProjectSerializer(projects, many=True).data)
