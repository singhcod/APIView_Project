
from django.shortcuts import render
from APIView_App.models import Employee
from APIView_App.serializers import EmployeeSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeListView(APIView):
    def get(self,request): # db --->> qs ---->> dict ---->> json ---->> browser
        employee_list = Employee.objects.all() # []  | [{},{},{},...]

        serializer = EmployeeSerializer(employee_list,many=True) # dict

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request): # browser ---->> json----->> dict---->>qs --->> db
        serilaizer = EmployeeSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeDetailView(APIView):
    def get(self,request,pk):
        try:
            employee = Employee.objects.get(id=pk)
        except Employee.DoesNotExist:
            data = {"message" : "Requested resource not available"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)

# code for resuability
    def get_object_by_id(self,pk):
        try:
            employee = Employee.objects.get(id=pk)
        except:
            employee = None
        return employee



    def put(self,request,pk):
        employee = self.get_object_by_id(pk) # employee object  |  None

        if employee is None:
            data = {"message": "Requested resource not available to update"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = EmployeeSerializer(employee , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        employee = self.get_object_by_id(pk)  # employee object  |  None
        if employee is None:
            data = {"message": "Requested resource not available to delete"}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            employee.delete()
            data = {"message": "Requested resource deleted successfully"}
            return Response(data, status=status.HTTP_204_NO_CONTENT)




