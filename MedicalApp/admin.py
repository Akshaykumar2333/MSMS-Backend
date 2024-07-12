from django.contrib import admin

from . import models
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'is_admin', 'is_employee', 'is_customer', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_employee', 'is_customer', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_employee', 'is_customer', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(models.Company )
admin.site.register(models.Medicine)
admin.site.register(models.MedicalDetails)
admin.site.register(models.Employee)
admin.site.register(models.Customer)
admin.site.register(models.Bill)
admin.site.register(models.EmployeeSalary)
admin.site.register(models.BillDetails)
admin.site.register(models.CustomerRequest)
admin.site.register(models.CompanyAccount)
admin.site.register(models.CompanyBank)
admin.site.register(models.EmployeeBank)
