from django.urls import path
from .views import UserList, UserDetail, CompanyNameByEmployees  # Import the new view

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),  # List and create users
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # Retrieve, update, delete user
    path('api/company-name/', CompanyNameByEmployees.as_view(), name='company-name-by-employees'),  # New endpoint
]