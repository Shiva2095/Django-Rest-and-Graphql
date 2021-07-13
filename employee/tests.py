import json
from employee.models import Employee
from employee.schema import EmployeeList

from django.test import TestCase

from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase

# Create your tests here.

def test_hey():
    client = Client(EmployeeList)
    executed = client.execute('''{ hey }''')
    assert executed == {
        'data': {
            'hey': 'hello!'
        }
    }


class EmployeeTest(TestCase):
    """ Test module for Employee model """

    def setUp(self):
        Employee.objects.create(emplyee_regNo=2,
                                emplyee_name="Ravi",
                                employee_email="ravi@gmail.com",
                                employee_mobile="7878788888")

        Employee.objects.create(emplyee_regNo=3,
                                emplyee_name="ROom",
                                employee_email="room@gmail.com",
                                employee_mobile="7878788889")

    def testEmployeeEmail(self):
        employee2 = Employee.objects.get(emplyee_regNo=2)
        employee3 = Employee.objects.get(emplyee_regNo=3)
        self.assertEqual(
            employee2.get_email(), "Ravi email address is ravi@gmail.com")
        self.assertEqual(
            employee3.get_email(), "ROom email address is room@gmail.com")


class MyFancyTestCase(GraphQLTestCase):
    def test_some_query(self):
        response = self.query(
            '''
            query {
                employees {
                    id
                    name
                    emplyeeRegno
                }
            }
            ''',
            # op_name='employees'
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
        ...

    def test_query_with_variables(self):
        response = self.query(
            '''
            query employee($id: Int!){
                employee(id: $id) {
                    id
                    emplyeeRegno
                }
            }
            ''',
            # op_name='employee',
            variables={'id': 1}
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)