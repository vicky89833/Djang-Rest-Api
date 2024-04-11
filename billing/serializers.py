from rest_framework import serializers
from .models import Bill
from products.models import Product
from django.db.models import F
from decimal import Decimal
from customers.models import Customer 
from rest_framework import serializers
from .models import Bill
from products.models import Product
from authentication.models import Employee  # Assuming you have an Employee model
from .models import PaymentMethod

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'name']

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'price', 'quantity']

class BillSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), default=serializers.CurrentUserDefault())
    print("employee object :" )
    class Meta:
        model = Bill
        fields = ['id', 'customer', 'product', 'quantity', 'total_amount', 'payment_method', 'employee']
        extra_kwargs = {'employee': {'write_only': True}}

    def validate_product(self, value):
        # Check if the product is available in the store
        if value.quantity < self.initial_data['quantity']:
            raise serializers.ValidationError("Not enough quantity available in the store.")
        return value

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        customer_data = validated_data.get('customer')
        if product is None:
            raise serializers.ValidationError("Product ID is required.")

        try:
            product = Product.objects.get(id=product)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product does not exist.")
        # Update product quantity in the store
        product.quantity -= quantity
        
        product.save()

        # Calculate total amount
        total_amount = product.price * quantity
        # Retrieve the authenticated user
        user = self.context['request'].user
        print("****************** user","*****************8")
        # Retrieve the corresponding Employee instance for the authenticated user
        try:
            employee = Employee.objects.get(user=user)
        except Employee.DoesNotExist:
            # Handle the case where the authenticated user is not an Employee
            raise serializers.ValidationError("Authenticated user is not an Employee.")
        validated_data['employee'] = employee
        
        if customer_data:
            # If customer data is provided, create or get the customer
            customer, _ = Customer.objects.get_or_create(**customer_data)
        else:
            # If customer data is not provided, raise a ValidationError
            raise serializers.ValidationError("Customer data is required.")
        
        # Retrieve payment method ID from validated data
        payment_method_id = validated_data.get('payment_method')
        if payment_method_id is None:
            raise serializers.ValidationError("Payment method ID is required.")

        try:
            # Retrieve payment method instance
            payment_method = PaymentMethod.objects.get(id=payment_method_id)
        except PaymentMethod.DoesNotExist:
            raise serializers.ValidationError("Payment method does not exist.")
        # Create bill object
        bill = Bill.objects.create(
            customer=validated_data['customer'],
            product=product,
            quantity=quantity,
            total_amount=total_amount,
            payment_method=validated_data['payment_method'],
            employee=validated_data['employee']  # Include the authenticated employee
        )
        print("bill is created ! ")
        # Increment total sold for the product
        Product.objects.filter(pk=product.pk).update(total_sold=F('total_sold') + quantity)

        product.save()
        return bill