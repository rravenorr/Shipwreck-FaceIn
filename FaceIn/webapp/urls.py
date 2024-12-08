
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('branch/<int:branch_id>/', views.branch_detail, name='branch_detail'),
    path('remove-shift/<int:employee_id>/<int:shift_id>/', views.remove_shift_from_employee, name='remove_shift'),
    path('add_shift/', views.add_shift, name='add_shift'),
    path('delete_shift/<int:shift_id>/', views.delete_shift, name='delete_shift'),
    path('add_employee_to_shift/', views.add_employee_to_shift, name='add_employee_to_shift'),
]
