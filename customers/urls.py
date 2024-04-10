from django.urls import path
from .views import CustomerListCreateView, CustomerRetrieveUpdateDeleteView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view() ,  name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name='customer-retrieve-update-delete'),
]