from django.db import models
from django import forms
from django.contrib.auth.models import User

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

    @property
    def employees(self):
        return self.department_employees.all()

    @property
    def shifts(self):
        return self.department_shifts.all()


class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True)
    shift_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_shifts')
    shift_expected_time_in = models.TimeField()
    shift_expected_time_out = models.TimeField()
    shift_day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])

    def __str__(self):
        return f"{self.shift_department} on {self.shift_day}: {self.shift_expected_time_in} - {self.shift_expected_time_out}"


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_comp_id = models.CharField(max_length=100)
    emp_Fname = models.CharField(max_length=100)
    emp_Lname = models.CharField(max_length=100)
    emp_Mname = models.CharField(max_length=100, blank=True, null=True)  # Optional middle name
    emp_sex = models.CharField(max_length=20, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    ])
    
    emp_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_employees')
    emp_role = models.CharField(max_length=20, choices=[
        ('Regular Employee', 'Regular Employee'),
        ('Department Head', 'Department Head'),
    ])

    emp_contact_no = models.CharField(max_length=20) 
    emp_date_hired = models.DateField()
    emp_leave_credits = models.IntegerField()
    emp_shift = models.ManyToManyField(Shift, related_name='shift_employees', blank=True)

    def __str__(self):
        return f"{self.emp_Fname} {self.emp_Lname}"  # Concatenate first and last name for better display
