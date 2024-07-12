
from django.contrib import admin
from django.urls import path,include
from MedicalApp import views
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import settings
from health_api import views as healthview



router=routers.DefaultRouter()
router.register("company",views.CompanyViewSet,basename="company")
router.register("companybank",views.CompanyBankViewset,basename="companybank")
router.register("medicine",views.MedicineViewSet,basename="medicine")
router.register("companyaccount",views.CompanyAccountViewset,basename="companyaccount")
router.register("employee",views.EmployeeViewset,basename="employee")
router.register("employee_all_bank",views.EmployeeBankViewset,basename="employee_all_bank")
router.register("employee_all_salary",views.EmployeeSalaryViewset,basename="employee_all_salary")
router.register("generate_bill_api",views.GenerateBillViewSet,basename="generate_bill_api")
router.register("customer_request",views.CustomerRequestViewSet,basename="customer_request")
router.register("home_api",views.HomeApiViewset,basename="home_api")

urlpatterns = [
    path('api/predict/', healthview.PredictAPIView.as_view(), name="predict"),
    path('api/users/<int:pk>/', views.UserListView.as_view(), name='user_details'),
    
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/gettoken/',views.CustomTokenObtainPairView.as_view(),name="gettoken"),
    path('api/refresh_token/',TokenRefreshView.as_view(),name="refresh_token"),
    path('api/companybyname/<str:name>',views.CompanyNameViewSet.as_view(),name="companybyname"),
    path('api/medicinebyname/<str:name>',views.MedicineNameViewSet.as_view(),name="medicinebyname"),
    path('api/get_name_id/<int:user_id>/', views.get_username_by_id, name='get_name_id'),
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/companyonly/',views.CompanyOnlyViewSet.as_view(),name="companyonly"),
    path('api/employee_bankby_id/<str:employee_id>',views.EmployeeBankByEIDViewSet.as_view(),name="employee_bankby_id"),
    path('api/employee_salaryby_id/<str:employee_id>',views.EmployeeSalaryByEIDViewSet.as_view(),name="employee_salaryby_id"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
