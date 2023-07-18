from django.urls import path
from employee.views import PersonApiView, PersonApiViewDetail
  
urlpatterns_employee = [
    path('v1/persons', PersonApiView.as_view()), 
    path('v1/persons/<int:id>', PersonApiViewDetail.as_view()), 
]