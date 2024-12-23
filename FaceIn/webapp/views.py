from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from collections import defaultdict
from .models import Department, Employee, Shift




# Create your views here.
def home(request):
    departments = Department.objects.all()  # Retrieve all departments
    return render(request, 'home.html', {'departments': departments})


def employees(request):
    employees = Employee.objects.all()
    return render(request, 'view_emp.html', {'employees': employees})

def add_employee(request):
    departments = Department.objects.all()
    return render(request, 'add_emp.html', {'departments': departments})


def department_detail(request, department_id):
    department = get_object_or_404(Department, department_id=department_id)
    employees = department.employees  # Dynamically fetch all employees for this department

    # Fetch all shifts for the department and group them by day
    shifts_by_day = defaultdict(list)
    shifts = department.shifts.all()
    for shift in shifts:
        shifts_by_day[shift.shift_day].append(shift)

    # Sort days to ensure proper order
    sorted_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ordered_shifts = {day: shifts_by_day[day] for day in sorted_days if day in shifts_by_day}

    return render(request, 'department.html', {'department': department, 'employees': employees, 'ordered_shifts': ordered_shifts})


def remove_shift_from_employee(request, employee_id, shift_id):
    employee = get_object_or_404(Employee, emp_id=employee_id)
    shift = get_object_or_404(Shift, shift_id=shift_id)
    
    # Remove the shift from the employee's emp_shift field
    employee.emp_shift.remove(shift)
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


def add_shift(request):
    if request.method == 'POST':
        department_id = request.POST.get('department_id')
        shift_day = request.POST.get('shift_day')
        shift_start = request.POST.get('shift_start')
        shift_end = request.POST.get('shift_end')

        if not department_id or not shift_day:
            messages.error(request, "Department ID or day is missing.")
            return redirect('home')

        try:
            department = Department.objects.get(department_id=department_id)
            Shift.objects.create(
                shift_department=department,
                shift_day=shift_day,
                shift_expected_time_in=shift_start,
                shift_expected_time_out=shift_end
            )
            messages.success(request, 'Shift added successfully!')
        except Department.DoesNotExist:
            messages.error(request, 'Invalid department selected.')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('department_detail', department_id=department_id)


def delete_shift(request, shift_id):
    try:
        shift = get_object_or_404(Shift, shift_id=shift_id)
        department_id = shift.shift_department.department_id  # Save department ID to redirect after deletion
        shift.delete()
        messages.success(request, 'Shift deleted successfully.')
        return redirect('department_detail', department_id=department_id)
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the shift: {e}")
        return redirect('home')


def add_employee_to_shift(request):
    if request.method == 'POST':
        shift_id = request.POST.get('shift_id')
        employee_id = request.POST.get('employee_id')

        try:
            shift = get_object_or_404(Shift, shift_id=shift_id)
            employee = get_object_or_404(Employee, emp_id=employee_id)

            # Add employee to the shift
            shift.shift_employees.add(employee)
            messages.success(request, f'{employee.emp_Fname} {employee.emp_Lname} has been added to the shift.')

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return redirect(request.META.get('HTTP_REFERER', '/'))


def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('department_name')

        try:
            # Create a new department
            Department.objects.create(
                department_name=department_name,
            )
            messages.success(request, "Department added successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('home')  # Redirect to the home page
    
def register_employee(request):
    if request.method == 'POST':
        # Collect form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        sex = request.POST.get('sex')
        contact_number = request.POST.get('contact')
        company_id = request.POST.get('comp_id')
        department_id = request.POST.get('department')  # Get department ID from POST
        role = request.POST.get('role')
        date_hired = request.POST.get('date_hires')
        leave_credits = request.POST.get('leave_credits')

        try:
            # Get department object using department_id
            department = Department.objects.get(department_id=department_id)
            
            # Create employee
            Employee.objects.create(
                emp_Fname=first_name,
                emp_Lname=last_name,
                emp_Mname=middle_name,
                emp_sex=sex,
                emp_contact_no=contact_number,  # Ensure field names match the model
                emp_comp_id=company_id,
                emp_department=department,
                emp_role=role,
                emp_date_hired=date_hired,
                emp_leave_credits=leave_credits,
            )

            # Add success message
            messages.success(request, "Employee added successfully!")
        except Department.DoesNotExist:
            messages.error(request, "Invalid department selected.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('home')  # Redirect to a success or home page

    # Get departments for the dropdown
    departments = Department.objects.all()
    return render(request, "register_employee.html", {'departments': departments})
