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
# 2. GET /employees/ to get all employee data
@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 3. GET /employees/<id>/ to get employee data by ID
# 4. PUT /employees/<id>/ to update employee data by ID
# 5. DELETE /employees/<id>/ to delete an employee
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
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
# 1. GET /departments/ to get all departments
# 2. POST /departments/ to create a department
@api_view(['GET', 'POST'])
def departments(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 3. GET /departments/<pk>/ to get department details
# 4. PUT /departments/<pk>/ to update department
# 5. DELETE /departments/<pk>/ to delete a department
@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Check if department has employees before deleting
        if department.employees.count() > 0:
            return Response({'error': 'Cannot delete department with employees.'}, status=400)
        
        department.delete()
        return Response(status=204)


# 6. GET /departments/<pk>/employees/ to get department details with employees
@api_view(['GET'])
def department_with_employees(request, pk):
    department = get_object_or_404(Department, pk=pk)

    serializer = DepartmentSerializer(department)
    employees = department.employees.all()  # Get all employees in this department
    employee_serializer = EmployeeSerializer(employees, many=True)
    
    data = serializer.data
    data['employees'] = employee_serializer.data  # Add employees to department response

    return Response(data)
# Project

# 1. GET /projects/ to get all projects
# 2. POST /projects/ to create a new project
@api_view(['GET', 'POST'])
def projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# 3. GET /projects/<id>/ to get project details
# 4. PUT /projects/<id>/ to update project status or add members
# 5. DELETE /projects/<id>/ to delete a project (only if end date has passed)
@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        new_status = request.data.get('status')
        employee_ids = request.data.get('employee_ids', [])

        if new_status:
            if new_status in ['NEW', 'ON-GOING', 'ENDED']:
                project.status = new_status
            else:
                return Response({'error': 'Invalid status'}, status=400)

        if employee_ids:
            employees = Employee.objects.filter(id__in=employee_ids)
            project.team.add(*employees)

        project.save()
        return Response({'message': 'Project updated successfully'})

    elif request.method == 'DELETE':
        if project.end_date <= date.today():
            project.delete()
            return Response({'message': 'Project deleted successfully'}, status=204)
        return Response({'error': 'Cannot delete project before end date'}, status=400)


# 6. GET /projects/<id>/budget/ to get the budget based on employee salaries
@api_view(['GET'])
def project_budget(request, id):
    project = get_object_or_404(Project, id=id)
    total_salary = sum(employee.salary for employee in project.team.all())
    return Response({'budget': total_salary})


# 7. GET /projects/status/NEW/ to get all "NEW" projects
# 8. GET /projects/status/ON-GOING/ to get all "ON-GOING" projects
# 9. GET /projects/status/ENDED/ to get all "ENDED" projects
@api_view(['GET'])
def project_status(request, status):
    if status not in ['NEW', 'ON-GOING', 'ENDED']:
        return Response({'error': 'Invalid status'}, status=400)

    projects = Project.objects.filter(status=status)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


# 10. GET /employees/highest-salary/ to get the highest salary employee
@api_view(['GET'])
def highest_salary(request):
    employee = Employee.objects.order_by('-salary').first()
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


# 11. GET /employees/second-highest-salary/ to get the second-highest salary by department
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


# 12. GET /departments/total-salary/ to get total salary under each department
@api_view(['GET'])
def total_salary_by_department(request):
    departments = Department.objects.all()
    total_salaries = {
        dept.name: dept.employees.aggregate(total_salary=Sum('salary'))['total_salary']
        for dept in departments
    }
    return Response(total_salaries)