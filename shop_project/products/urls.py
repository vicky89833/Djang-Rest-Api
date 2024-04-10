from django.urls import path
from .views import ProductCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-delete'),
]
