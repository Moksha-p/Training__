from django.db import models

# Department Model
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Employee Model
class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
       
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    salary = models.FloatField()
    designation = models.CharField(max_length=255, choices=DESIGNATION_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255)
    projects = models.ManyToManyField('Project', related_name='employees', blank=True)

    def __str__(self):
        return self.name

# Project Model
class Project(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ON-GOING', 'On-going'),
        ('ENDED', 'Ended'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    team = models.ManyToManyField(Employee, related_name='projects_team', null=True, blank=True)  # Use related_name for reverse relation
    team_lead = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='team_lead_projects', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
