from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Get list of users and insert a user
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get a single user by ID, update, or delete a user
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# New view to get company name by employee IDs
class CompanyNameByEmployees(generics.ListAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        employee_ids = request.query_params.getlist('employees')  # Get employee IDs from query params
        if not employee_ids:
            return Response({"detail": "No employee IDs provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Filter users based on the provided employee IDs
        users = User.objects.filter(employees__contains=employee_ids)  # Assuming employees is a JSONField
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)