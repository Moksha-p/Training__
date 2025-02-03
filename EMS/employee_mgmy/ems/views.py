from django.shortcuts import render
from .models import Employee, Department, Project
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework import status, request
from rest_framework.response import Response
from datetime import date
from django.shortcuts import get_object_or_404
from django.db.models import Sum
# Create your views here.


# @api_view(['GET'])
# def get_employees(request):
#     employees = Employee.objects.all()
#     serializers = EmployeeSerializer(employees, many = True)
#     return response.Response(serializers.data)

# 1. POST /employees/ to create an employee
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# 2. GET /employees/ to get all employee data
@api_view(['GET'])
def get_all_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

# 3. PUT /employees/<id>/ to update employee data by ID
@api_view(['PUT'])
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# 4. GET /employees/<id>/ to get employee data by ID
@api_view(['GET'])
def get_employee_by_id(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

# 5. DELETE /employees/<id>/ to delete an employee
@api_view(['DELETE'])
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=204)

# 6. GET /employees/<id>/department/ to get department details by employee ID
@api_view(['GET'])
def get_employee_department(request, id):
    employee = get_object_or_404(Employee, id=id)
    department = employee.department
    department_data = {
        'id': department.id,
        'name': department.name
    }
    return Response(department_data)

# Department
@api_view(['POST'])
def create_department(request):
    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def get_departments(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
def update_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=404)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_department_with_employees(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        employees = department.employees.all()  # Get all employees related to this department
        employee_serializer = EmployeeSerializer(employees, many=True)
        
        data = serializer.data
        data['employees'] = employee_serializer.data  # Add employee data to the department response
        
        return Response(data)

@api_view(['DELETE'])
def delete_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except Department.DoesNotExist:
        return Response(status=404)

    # Check if there are any employees in the department before deleting
    if department.employees.count() > 0:
        return Response({'error': 'Cannot delete department with employees.'}, status=400)

    if request.method == 'DELETE':
        department.delete()
        return Response(status=204)

# Project

# 1. POST /projects/ to create a new project
@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 2. GET /projects/ to get all projects (with team members data)
@api_view(['GET'])
def get_all_projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


# 3. PUT /projects/<id>/add-member/ to add a new member to the project
@api_view(['PUT'])
def add_member_to_project(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'PUT':
        employee_ids = request.data.get('employee_ids', [])
        employees = Employee.objects.filter(id__in=employee_ids)
        project.team.add(*employees)
        return Response({'message': 'Members added successfully'})


# 4. GET /projects/<id>/ to get project details by ID
@api_view(['GET'])
def get_project_by_id(request, id):
    project = get_object_or_404(Project, id=id)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


# 5. DELETE /projects/<id>/ to delete a project (only if the end date has passed)
@api_view(['DELETE'])
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if project.end_date <= date.today():
        if request.method == 'DELETE':
            project.delete()
            return Response({'message': 'Project deleted successfully'}, status=204)
    else:
        return Response({'error': 'Cannot delete project before end date'}, status=400)


# 6. PUT /projects/<id>/update-status/ to update the status of the project
@api_view(['PUT'])
def update_project_status(request, id):
    project = get_object_or_404(Project, id=id)
    new_status = request.data.get('status')
    if new_status in ['NEW', 'ON-GOING', 'ENDED']:
        project.status = new_status
        project.save()
        return Response({'message': 'Project status updated successfully'})
    return Response({'error': 'Invalid status'}, status=400)


# 7. GET /projects/<id>/budget/ to get the budget of the project based on employee salaries
@api_view(['GET'])
def get_project_budget(request, id):
    project = get_object_or_404(Project, id=id)
    total_salary = sum(employee.salary for employee in project.team.all())
    return Response({'budget': total_salary})


# 8. GET /employees/highest-salary/ to get the highest salary holders
@api_view(['GET'])
def highest_salary(request):
    employee = Employee.objects.order_by('-salary').first()
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


# 9. GET /employees/second-highest-salary/ to get the second-highest salary holder grouped by department
@api_view(['GET'])
def second_highest_salary_by_department(request):
    departments = Department.objects.all()
    result = {}

    for dept in departments:
        employees = dept.employees.order_by('-salary')
        if employees.count() > 1:
            second_highest = employees[1]
            result[dept.name] = EmployeeSerializer(second_highest).data

    return Response(result)


# 10. GET /departments/total-salary/ to get the total salary of employees under each department
@api_view(['GET'])
def total_salary_by_department(request):
    departments = Department.objects.all()
    total_salaries = {}

    for dept in departments:
        total_salary = dept.employees.aggregate(total_salary=Sum('salary'))['total_salary']
        total_salaries[dept.name] = total_salary

    return Response(total_salaries)


# 11. GET /projects/new/ to get all "NEW" projects
@api_view(['GET'])
def get_new_projects(request):
    projects = Project.objects.filter(status='NEW')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# 12. GET /projects/on-going/ to get all "ON-GOING" projects
@api_view(['GET'])
def get_ongoing_projects(request):
    projects = Project.objects.filter(status='ON-GOING')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# 13. GET /projects/ended/ to get all "ENDED" projects
@api_view(['GET'])
def get_ended_projects(request):
    projects = Project.objects.filter(status='ENDED')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)