import graphene
from employee.models import Employee
from employee import types
from employee.mutations import EmployeeCreate



class EmployeeList(graphene.ObjectType):
    employees = graphene.List(types.EmployeeType)
    employee = graphene.Field(types.EmployeeType, id=graphene.Int())

    def resolve_employees(root, info):
        return Employee.objects.all()

    def resolve_employee(root, info, id):
        try:
            employee = Employee.objects.get(id=id)
            return employee
        except Employee.DoesNotExist:
            return None


class EmployeeMutations(graphene.ObjectType):
    ''' Add Customer related Mutations here '''
    employee_create = EmployeeCreate.Field()
