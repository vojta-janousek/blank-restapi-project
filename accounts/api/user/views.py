from django.contrib.auth import get_user_model

from rest_framework import permissions, generics

from accounts.api.user.serializers import UserDetailSerializer
from accounts.api.permissions import AnonPermissionOnly

from status.api.serializers import StatusInlineUserSerializer
from status.models import Status


User = get_user_model()


class UserDetailApiView(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'


class UserStatusApiView(generics.ListAPIView):
    serializer_class = StatusInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)