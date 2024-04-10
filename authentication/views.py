from django.shortcuts import render



# For empolyee
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer ,EmployeeTokenObtainPairSerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]  # Only admin users can list and create employees

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]  # Any authenticated user can retrieve, update, or delete an employee


from rest_framework_simplejwt.views import TokenObtainPairView

class EmployeeTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmployeeTokenObtainPairSerializer  # Replace with your serializer class

employee_token_obtain_pair = EmployeeTokenObtainPairView.as_view()

