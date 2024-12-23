
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('remove-shift/<int:employee_id>/<int:shift_id>/', views.remove_shift_from_employee, name='remove_shift'),
    path('add_shift/', views.add_shift, name='add_shift'),
    path('delete_shift/<int:shift_id>/', views.delete_shift, name='delete_shift'),
    path('add_employee_to_shift/', views.add_employee_to_shift, name='add_employee_to_shift'),
    path('employees/', views.employees, name='employees'),
    path('add_department/', views.add_department, name='add_department'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('add_employee/', views.add_employee, name='add_employee'),
]
