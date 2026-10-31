from django.db import router
from django.urls import path, include
from . import views 
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register('employees', views.EmployeeViewSet, basename='employee')
urlpatterns = [
    path('students/', views.studentsView, name='studentsView'),#GET, POST
    path('students/<int:pk>/', views.StudentDetailView, name='StudentDetailView'), #GET, PUT, DELETE
    
    # Class Based Views URLs
     path('employees/', views.Employees.as_view(), name='employees'),
     path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-detail'),
     #path('', include(router.urls)), # viewsets



]