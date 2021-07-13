import graphene
from graphene_django import DjangoObjectType

from employee.models import Employee

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = "__all__"
        