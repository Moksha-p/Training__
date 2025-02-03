from django.db import models

# Create your models here.
class Department(models.Model):
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    
    class Meta:
        db_table =  "Department"
    
    def __str__(self):
        return self.name


    
class Employee(models.Model):
    
    # gender_choices = [
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('O', 'Other')
    # ]
    
    # age = models.IntegerField()
    # email = models.EmailField()
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    salary =  models.FloatField()
    designation =  models.CharField(max_length = 20)
    address = models.CharField(max_length = 225)
    department = models.ForeignKey(Department, related_name = "employees", on_delete = models.CASCADE)
    project =  models.ManyToManyField('Project', related_name = "employees", blank = True)
    
    # gender = models.CharField(max_length = 1, choices = gender_choices)
    
    class Meta:
        db_table =  "Employee"

    def __str__(self):
        return f'{self.id} - {self.name} - {self.designation} - {self.department} - {self.project}'
    

    
class Project(models.Model):
    

    
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ON-GOING', 'On-Going'),
        ('ENDED', 'Ended'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    team = models.ManyToManyField(Employee, related_name='projects_team', blank=True)
    team_lead = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='lead_projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name