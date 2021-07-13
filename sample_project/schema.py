import graphene
from graphene.types.mutation import Mutation
from employee import mutations
from employee.schema import EmployeeList
from employee.schema import EmployeeMutations

class Query(EmployeeList, graphene.ObjectType):
    pass

class Mutations(EmployeeMutations):
    pass

schema = graphene.Schema(Query, Mutations)