from django.urls import path,include
from rest_framework.routers import DefaultRouter
from  . import views

# router = DefaultRouter()
# router.register(r'employees', EmployeeViewSet)
# router.register(r'departments', DepartmentViewSet)
# router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # Employee related URLs
    path('employees/', views.create_employee, name='create-employee'),  # POST /employees/
    path('employees/', views.get_all_employees, name='employee-list'),  # GET /employees/
    path('employees/<int:id>/', views.update_employee, name='update-employee'),  # PUT /employees/<id>/
    path('employees/<int:id>/', views.get_employee_by_id, name='employee-detail'),  # GET /employees/<id>/
    path('employees/<int:id>/delete/', views.delete_employee, name='delete-employee'),  # DELETE /employees/<id>/
    path('employees/<int:id>/department/', views.get_employee_department, name='employee-department'),  # GET /employees/<id>/department/
    # Department
    path('departments/', views.create_department, name='create-department'),
    path('departments/', views.get_departments, name='department-list'),
    path('departments/<int:pk>/', views.update_department, name='update-department'),
    path('departments/<int:pk>/', views.get_department_with_employees, name='department-with-employees'),
    path('departments/<int:pk>/', views.delete_department, name='delete-department'),
    
    
    # Project related URLs
    path('projects/', views.create_project, name='create-project'),  # POST /projects/
    path('projects/', views.get_all_projects, name='project-list'),  # GET /projects/
    path('projects/<int:id>/add-member/', views.add_member_to_project, name='add-member-to-project'),  # PUT /projects/<id>/add-member/
    path('projects/<int:id>/', views.get_project_by_id, name='project-detail'),  # GET /projects/<id>/
    path('projects/<int:id>/delete/', views.delete_project, name='delete-project'),  # DELETE /projects/<id>/
    path('projects/<int:id>/update-status/', views.update_project_status, name='update-project-status'),  # PUT /projects/<id>/update-status/
    path('projects/<int:id>/budget/', views.get_project_budget, name='get-project-budget'),  # GET /projects/<id>/budget/
    
    # Employee-related URLs
    path('employees/highest-salary/', views.highest_salary, name='highest-salary'),  # GET /employees/highest-salary/
    path('employees/second-highest-salary/', views.second_highest_salary_by_department, name='second-highest-salary'),  # GET /employees/second-highest-salary/
    
    # Department-related URLs
    path('departments/total-salary/', views.total_salary_by_department, name='total-salary-department'),  # GET /departments/total-salary/
    
    # Project status-related URLs
    path('projects/new/', views.get_new_projects, name='new-projects'),  # GET /projects/new/
    path('projects/on-going/', views.get_ongoing_projects, name='ongoing-projects'),  # GET /projects/on-going/
    path('projects/ended/', views.get_ended_projects, name='ended-projects'),  # GET /projects/ended/
]
