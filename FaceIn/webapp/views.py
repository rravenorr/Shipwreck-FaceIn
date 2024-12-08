from django.shortcuts import render
from .models import Branch  # Import your Branch model
from django.shortcuts import render, get_object_or_404, redirect
from collections import defaultdict
from .models import Employee, Shift
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shift, Branch


# Create your views here.
def home(request):
    branches = Branch.objects.all()  # Retrieve all branches
    return render(request, 'home.html', {'branches': branches})


# In your view
from collections import defaultdict

def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, branch_id=branch_id)
    employees = branch.employees  # Dynamically fetch all employees for this branch

    # Fetch all shifts for the branch and group them by day
    shifts_by_day = defaultdict(list)
    shifts = branch.shifts.all()
    for shift in shifts:
        shifts_by_day[shift.shift_day].append(shift)

    # Sort days to ensure proper order
    sorted_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ordered_shifts = {day: shifts_by_day[day] for day in sorted_days if day in shifts_by_day}

    return render(request, 'branch.html', {'branch': branch, 'employees': employees, 'ordered_shifts': ordered_shifts})

def remove_shift_from_employee(request, employee_id, shift_id):
    employee = get_object_or_404(Employee, emp_id=employee_id)
    shift = get_object_or_404(Shift, shift_id=shift_id)
    
    # Remove the shift from the employee's emp_shift field
    employee.emp_shift.remove(shift)
    
    # Optionally, redirect to the branch page or where needed
    return redirect(request.META.get('HTTP_REFERER', '/'))

def add_shift(request):
    if request.method == 'POST':
        branch_id = request.POST.get('branch_id')
        shift_day = request.POST.get('shift_day')
        shift_start = request.POST.get('shift_start')
        shift_end = request.POST.get('shift_end')

        if not branch_id or not shift_day:
            messages.error(request, "Branch ID or day is missing.")
            return redirect('home')

        try:
            branch = Branch.objects.get(branch_id=branch_id)
            Shift.objects.create(
                branch=branch,
                shift_day=shift_day,
                shift_start=shift_start,
                shift_end=shift_end
            )
            messages.success(request, 'Shift added successfully!')
        except Branch.DoesNotExist:
            messages.error(request, 'Invalid branch selected.')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('branch_detail', branch_id=branch_id)

def delete_shift(request, shift_id):
    try:
        shift = get_object_or_404(Shift, shift_id=shift_id)
        branch_id = shift.branch.branch_id  # Save branch ID to redirect after deletion
        shift.delete()
        messages.success(request, 'Shift deleted successfully.')
        return redirect('branch_detail', branch_id=branch_id)
    except Exception as e:
        messages.error(request, f"An error occurred while deleting the shift: {e}")
        return redirect('home')
    
def add_employee_to_shift(request):
    print("adding employee to shift")
    if request.method == 'POST':
        shift_id = request.POST.get('shift_id')
        employee_id = request.POST.get('employee_id')

        try:
            shift = get_object_or_404(Shift, shift_id=shift_id)
            employee = get_object_or_404(Employee, emp_id=employee_id)

            # Add employee to the shift
            shift.shift_employees.add(employee)
            messages.success(request, f'{employee.emp_name} has been added to the shift.')

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return redirect(request.META.get('HTTP_REFERER', '/'))

