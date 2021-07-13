from logging import error
import graphene
from employee import types
from employee.models import Employee


class EmployeeCreate(graphene.Mutation):
    class Arguments:
         reg_no = graphene.Int(required=True)
         name = graphene.String(required=True)
         email = graphene.String(required=True)
         mobile = graphene.String(required=True)

    errors = graphene.String()
    employee = graphene.Field(types.EmployeeType)

    @staticmethod
    def mutate(root, info, reg_no, name, email, mobile):
        try:
            employee = Employee.objects.create(emplyee_regNo=reg_no,
                                                emplyee_name=name,
                                                employee_email=email,
                                                employee_mobile=mobile

            )
            return EmployeeCreate(employee=employee, errors=None)
        except:
            return EmployeeCreate(employee=None, errors="Arguments not Valid")
