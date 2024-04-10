from django.urls import path
from .views import (
    EmployeeListCreateAPIView,
    EmployeeDetailAPIView,
    EmployeeTokenObtainPairView
)

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-retrieve-update-destroy'),
    path('token/', EmployeeTokenObtainPairView.as_view(), name='token_obtain_pair'),
]

