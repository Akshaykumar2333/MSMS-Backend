from rest_framework import serializers
from MedicalApp.models import (Company, CompanyBank, Medicine, MedicalDetails, Employee, Customer, Bill,
CustomerRequest, CompanyAccount, EmployeeBank, EmployeeSalary, BillDetails)

# companyserializer
class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

#companybankserializer
class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyBank
        fields="__all__"
        


# medicine serilaizer

class MedicineSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerliazer(instance.company_id).data
        return response
    
#  medical details serializer
class MedicalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalDetails
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['medicine'] = MedicineSerliazer(instance.medicine_id).data
        return response

# mdeical details simple serializer
class MedicalDetailsSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model=MedicalDetails
        fields="__all__"


# employee serializer
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"


# customer serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"


# bill serializer
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer_id).data
        return response


# customer request serializer
class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerRequest
        fields="__all__"


# comanpy account serilaizer
class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyAccount
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerliazer(instance.company_id).data
        return response


# employee bank serializer
class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeBank
        fields="__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response


# employee salary serializer
class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeSalary
        fields="__all__"

# bill details serializer
class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillDetails
        fields="__all__"



# serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers







from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    is_admin = serializers.BooleanField(write_only=True, default=False)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2', 'is_admin', 'is_employee', 'is_customer','email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        
        is_admin = validated_data.pop('is_admin', False)


        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=password,
            is_admin=validated_data.get('is_admin', False),
            is_employee=validated_data.get('is_employee', False),
            is_customer=validated_data.get('is_customer', False),
            email=validated_data['email']
        )
        if is_admin:
            user.is_staff = True
            user.is_admin=True
            user.is_superuser=True
            user.save()

        return user
    
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'is_admin', 'is_employee', 'is_customer','email']


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['user_id'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({'user_id': self.user.id})
        return data
