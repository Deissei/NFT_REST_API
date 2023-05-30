from django.contrib.auth import get_user_model
from rest_framework import mixins, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.users.serializers import (UserCreateSerializer, UserSerializer,
                                    UserUpdatePasswordSerializer)
from utils.permissions import IsOwner

User = get_user_model()


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == "update_password":
            return UserUpdatePasswordSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'update_password'):
            return [IsOwner()]
        return [permissions.AllowAny()]
    
    @action(detail=True, methods=['PUT', 'PATCH'])
    def update_password(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password1']
        user.set_password(new_password)
        serializer.save()
        return Response({'message': 'Password updated successfully.'})
