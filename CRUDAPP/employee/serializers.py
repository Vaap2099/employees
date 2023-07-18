from rest_framework.serializers import ModelSerializer
from employee.models import Employee


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Employee
        #fields = [EmpId, Name, LastName, Address, HomeTel, MobileTel, State, BusinessId, DepartmentId, UnitId ]
        fields = '__all__'