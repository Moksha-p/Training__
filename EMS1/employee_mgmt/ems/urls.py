from django.urls import path,include
from rest_framework.routers import DefaultRouter
from  . import views

# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # Employee related URLs
    
    path('employees/', views.employees, name='employees'),
    path('employees/<int:id>/', views.employee_detail, name='employee-detail'),
    path('employees/<int:id>/department/', views.get_employee_department, name='employee-department'),
    # Department
    
    path('departments/', views.departments, name='departments'),
    path('departments/<int:pk>/', views.department_detail, name='department-detail'),
    path('departments/<int:pk>/employees/', views.department_with_employees, name='department-with-employees'),
    
    
    # Project related URLs
   
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.project_detail, name='project-detail'),
    path('projects/<int:id>/budget/', views.project_budget, name='project-budget'),
    path('projects/status/<str:status>/', views.project_status, name='project-status'),

    path('employees/highest-salary/', views.highest_salary, name='highest-salary'),
    path('employees/second-highest-salary/', views.second_highest_salary_by_department, name='second-highest-salary'),
    
    path('departments/total-salary/', views.total_salary_by_department, name='total-salary-by-department'),
]
