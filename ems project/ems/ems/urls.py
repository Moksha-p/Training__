from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import EmployeeViewSet, DepartmentViewSet, ProjectViewSet
from accounts.views import total_salary_per_department, get_new_projects, get_ongoing_projects, get_ended_projects

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employees')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('departments/total-salary/', total_salary_per_department),
    path('projects/new/', get_new_projects),
    path('projects/on-going/', get_ongoing_projects),
    path('projects/ended/', get_ended_projects),
]
