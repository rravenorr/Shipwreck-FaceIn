from django.contrib import admin
from .models import Department, Employee, Shift

# Register models
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    search_fields = ('department_name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_Fname', 'emp_Lname', 'emp_department', 'emp_sex')
    search_fields = ('emp_Fname', 'emp_Lname', 'emp_department__department_name')
    list_filter = ('emp_department', 'emp_sex')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shift_day', 'shift_expected_time_in', 'shift_expected_time_out', 'shift_department')
    list_filter = ('shift_day', 'shift_department')
