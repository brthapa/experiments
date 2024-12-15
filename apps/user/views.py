from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@extend_schema_view(
    list=extend_schema(description="Retrieve list of user profiles"),
    retrieve=extend_schema(description="Retrieve a single user profile"),
    create=extend_schema(description="Create a new user profile"),
    update=extend_schema(description="Update a user profile"),
    partial_update=extend_schema(description="Partially update a user profile"),
    destroy=extend_schema(description="Delete a user profile")
)
@permission_classes([IsAuthenticated])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer