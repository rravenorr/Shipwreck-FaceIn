from django.contrib import admin
from .models import Branch, Employee, Shift

# Register models
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_address', 'branch_ip')
    search_fields = ('branch_name', 'branch_address')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'emp_email', 'emp_branch')
    search_fields = ('emp_name', 'emp_email')
    list_filter = ('emp_branch',)

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('shift_day', 'shift_start', 'shift_end')
    list_filter = ('shift_day',)
# Register your models here.
