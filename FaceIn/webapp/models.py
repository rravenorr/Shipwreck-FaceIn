from django.db import models

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)
    branch_address = models.CharField(max_length=100)
    branch_ip = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name

    @property
    def employees(self):
        return self.branch_employees.all()  # Use the related_name for the ForeignKey in Employee

class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    shift_day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='shifts')

    def __str__(self):
        return f"{self.branch} on {self.shift_day}: {self.shift_start} - {self.shift_end}"


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)
    emp_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch_employees')
    emp_shift = models.ManyToManyField(Shift, related_name='shift_employees', blank=True)

    def __str__(self):
        return self.emp_name
