from django.urls import path

from .views import BillingCreateView, BillingRetrieveUpdateDestroyView , PaymentMethodListCreateAPIView, PaymentMethodRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('bills/', BillingCreateView.as_view(), name='bill-create'),
    path('bills/<int:pk>/', BillingRetrieveUpdateDestroyView.as_view(), name='bill-retrieve-update-delete'),
    path('payment-methods/', PaymentMethodListCreateAPIView.as_view(), name='payment-method-list-create'),
    path('payment-methods/<int:pk>/', PaymentMethodRetrieveUpdateDestroyAPIView.as_view(), name='payment-method-detail'),

]
