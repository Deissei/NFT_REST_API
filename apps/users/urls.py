from rest_framework import routers
from django.urls import path
from apps.users.views import UserAPIViewSet


router = routers.DefaultRouter()

router.register('', UserAPIViewSet)

urlpatterns = [
    path('users/<int:pk>/update-password', UserAPIViewSet.as_view({'put' : 'update_password', 'patch' : 'update_password'}), name="update-password"),
]

urlpatterns = router.urls
