from django.urls import path
from . import views

urlpatterns = [
    path('employeeslist/', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('engineers/', views.employee_engineers, name='employee_engineers'),
    path('add/', views.create_employee, name='employee-add'),
    path('addproject/', views.create_project, name='project-add'),

    #path('success/', views.employee_success, name='employee_success'),
]