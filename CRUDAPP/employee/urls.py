from django.urls import path
from employee.views import EmployeeApiView, EmployeeApiViewDetail
  
urlpatterns_employee = [
    path('v1/employee', EmployeeApiView.as_view()), 
    path('v1/employee/<int:id>', EmployeeApiViewDetail.as_view()), 
]