# Django-Rest-and-Graphql
﻿# 1.                                                       Django Project Setup With virtual environment:


1. ``` mkdir {project_name}.```

##### To install virtual Environment
2. ``` sudo apt-get install python3-venv ```
    
#####  To create virtual env directory
3. ``` python3 -m venv djangoenv ```
    
##### to activate virtual environment
4. ``` source djangoenv/bin/activate ```

##### To deactivate virtual environment
5. ``` deactivate ```
	
##### Now we are installing Django in our virtual Env
6. ``` pip install django ```
 	
##### To Create a new Project 
7. ```  django-admin startproject {project_name}  ```
   ```  eg. django-admin startproject sample_project ```
	
##### This command is used to runsserver of django
8.  ``` python manage.py runserver  ```
  	
##### To create tables in database,  by default we have a user table  in django project
9. ``` python manage.py makemigrations 
       python manage.py migrate ```

After adding we to apply migrate.
```
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  ```
	
Default this migration is apply on migrate 

Now Our projects basic Setup is Done 
	
##### This command is used to Create a Super user to access django default admin panel
10.  ``` python manage.py createsuperuser ```
	
##### To create a new application in our project 
11. ``` django-admin startapp {app_name} ```
	

##### After creating new app we have to add this app in installed_apps in settings.py file

----------------------------------------------------------------------------xxxxx---------------------------------------------------------------------------------

# 2.                                                               Django REST Framework Setup :

##### First we have install django rest framework in our Virtual Environment

##### to install  django rest framework in our Virtual Environment
1. ``` pip install djangorestframework.```
 	
##### We can check what we have installed in our env
2. ``` pip freeze ```
	
##### we have to add rest_framework in installed apps settings.py file
3.  ```
	INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'employee',   
                'rest_framework',
       ]
       ```

##### DRF CRUD Operation .


##### Create Serializer.py file in app.
1. 
```
from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
      class Meta:
            model = Employee
            fields = '__all__'
```


##### We are creating Crud Operation with APIview class based
2.  Go in th views.py file
	
3. CRUD(Create, Retrieve, Update, Delete)

4. 
  ```
  class EmployeesCrud(APIView):
  """
  View to list all users in the system.

  * Requires token authentication.
  * Only admin users are able to access this view.
  """
  def get_object(self, pk):
    return Employee.objects.get(id=pk)
      ```
  ##### Creating class called EmployeeCrud and get_object method in it to get data 

##### Retrieve:

5. ``` 
   def get(self, request,pk=None, format=None):
      """
      Return a list of all users.
      """
      if pk is None:
        usernames = Employee.objects.all()
         print("usernames", usernames)
         serializer = EmployeeSerializer(usernames, many=True)
         return Response(serializer.data)
      else:
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
```
 
##### with method we are creating fetch data api 

##### Create:
6. 
```
def post(self, request, pk=None, format=None):
  """
  create a New Employee
  """
  serializer = EmployeeSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
##### This method is used to create a new Entry in a table called Employee

##### Update (Put, Patch):
7. 
```
def patch(self, request, pk):
  """
  Update partially a New Employee
  """
  employeemodel_object = self.get_object(pk)
  serializer = EmployeeSerializer(employeemodel_object, data=request.data, partial=True) # set partial=True to update a data partially
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def put(self, request, pk, format=None):
  """
  update a Employee
  """
  employee = self.get_object(pk)
  serializer = EmployeeSerializer(employee, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

These two method is used to update the Employee table entry,  with Put method we update whole entry and with Patch Method we can update partial field update.

##### Delete:
8.  
```
def delete(self, request, pk, format=None):
  """
  delete a Employee
  """
  employee = self.get_object(pk)
  employee.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
```

This method is used to delete a Entry


##### After Creating Class and method we have to create a url for it .
9 . 
In `urls.py` file of a Employee app
```
from employee import views

path('employee/', views.EmployeesCrud.as_view(), name='employeecrud'),

```
This url is used for without getting data by Id 

10.  ```path('employee/<int:pk>/', views.EmployeesCrud.as_view(), name='employeecrud') ```
	
this url is used when we update the particular data so we given ID for them so we created this url for that.

----------------------------------------------------------------------------xxxxx---------------------------------------------------------------------------------
# 3.                                                      Graphql Setup and Create Queries and mutations.

##### To install in your Virtual Environment and Locally also
1. ``` pip install graphene-django ```
  

##### Add graphene django  to the installed apps  in settings.py file of your Django Project
2.   
```
INSTALLED_APPS = [
            "django.contrib.staticfiles", # Required for GraphiQL
            "graphene_django”
]
```

##### We need to add a graphql URL to the urls.py file of your django Project.
```
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
        path('admin/', admin.site.urls),
        path('graphql/', GraphQLView.as_view(graphiql=True)),
        # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
        path('employee/', views.EmployeesCrud.as_view(), name='employeecrud'),
        path('employee/<int:pk>/', views.EmployeesCrud.as_view(), name='employeecrud')
]
```
##### Change `graphiql=True` to `graphiql=False` if you do not want to use the GraphiQL API browser.


##### Finally, define the schema location for Graphene in the Settings.py file of your Django project:
3.
```
GRAPHENE = {
"SCHEMA": "sample_project.schema.schema"
}
```

Now our Basic Setup is Done.

#####  First we have to create the types.py file in our APP eg: employee in my Sample_project.

##### We define the type of Every model for which we want to add Query or Mutation
```
import graphene
from graphene_django import DjangoObjectType

from employee.models import Employee

class EmployeeType(DjangoObjectType):
  class Meta:
    model = Employee
    fields = "__all__"
```
##### Now we create a schema.py file in our App . schema.py file is used to create a queries
7. 
```
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
```
##### Now we create a mutations.py file in our App. To create a Mutations
8. 
```
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
```
##### After creating mutation we should add this mutation class in schema file like this :

9. 
```
class EmployeeMutations(graphene.ObjectType):
''' Add Customer related Mutations here '''
    employee_create = EmployeeCreate.Field()
```

##### Now we create a new schema.py file in our project level so that we can run all queries and muatation.
10.  
```
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

```

##### Now we can Run Our queries and mutations
11. To run Queries and Mutation .
	``` http://localhost:8000/graphql ```


##### Now To test Graphql API’s

##### In our app their is one tests.py file is already created so we write test cases here.
12.  
```
import json
from employee.models import Employee
from employee.schema import EmployeeList

from django.test import TestCase

from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase


class MyFancyTestCase(GraphQLTestCase):
  def test_some_query(self):
    response = self.query(
    '''
    query {
    employees {
    id
    emplyeeName
    emplyeeRegno
    }
    }
    ''',
    )

    content = json.loads(response.content)

    # This validates the status code and if you get errors
    self.assertResponseNoErrors(response)

##### Add some more asserts if you like
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
    variables={'id': 1}
    )

    content = json.loads(response.content)

    # This validates the status code and if you get errors
    self.assertResponseNoErrors(response)
```
##### You can run this test cases by:
12.  
 ``` python manage.py test ```
 
#####  If your Test cases run successfully then out will be.
13.
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.013s

OK
Destroying test database for alias 'default'...
```
##### If any test case fail then error will be like:
14.  
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..F
======================================================================
FAIL: test_some_query (employee.tests.MyFancyTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/erangle/Downloads/projects/sample_project/employee/tests.py", line 63, in test_some_query
    self.assertResponseNoErrors(response)
  File "/home/erangle/Downloads/projects/sample_project/sample_project/lib/python3.6/site-packages/graphene_django/utils/testing.py", line 117, in assertResponseNoErrors
    self.assertEqual(resp.status_code, 200, msg or content)
AssertionError: 400 != 200 : {'errors': [{'message': 'Cannot query field "name" on type "EmployeeType".', 'locations': [{'line': 5, 'column': 21}]}]}

----------------------------------------------------------------------
Ran 3 tests in 0.016s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
##### Test case for basic Models testing
15.
```
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
    employee2.get_email(), "ravi email address is ravi@gmail.com")
    self.assertEqual(
    employee3.get_email(), "ROom email address is room@gmail.com")


```
