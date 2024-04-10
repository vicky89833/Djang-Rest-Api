from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  # For hashing passwords
from .models import Employee

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Make password writable
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # You can add more fields if needed

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        return User.objects.create(**validated_data)

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer to include user information

    class Meta:
        model = Employee
        fields = ['id', 'user', 'department', 'position', 'total_sell']  # Fields from the Employee model

    def create(self, validated_data):
        user_data = validated_data.pop('user')  # Extract user data
        user_serializer = UserSerializer(data=user_data)  # Create user serializer instance
        if user_serializer.is_valid():
            user = user_serializer.save()  # Save user
            employee = Employee.objects.create(user=user, **validated_data)  # Create employee
            return employee
        else:
            raise serializers.ValidationError(user_serializer.errors)


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EmployeeTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims if needed
        token['username'] = user.username
        # Add more claims as necessary

        return token
