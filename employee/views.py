from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import status
from django.http import Http404


class EmployeesCrud(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get_object(self, pk):
        return Employee.objects.get(id=pk)

    def get(self, request,pk=None, format=None):
        """
        Return a list of all users.
        """
        if pk is None:
            usernames =  Employee.objects.all()
            serializer = EmployeeSerializer(usernames, many=True)
            return Response(serializer.data)
        else:
            employee = self.get_object(pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)

    def post(self, request, pk=None, format=None):
        """
        create a New Employee
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        update a  Employee
        """
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        delete a  Employee
        """
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)