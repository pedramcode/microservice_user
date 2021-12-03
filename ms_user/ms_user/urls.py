from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user.views import UserViewSet, ProfileViewSet

router = SimpleRouter()
router.register("user", UserViewSet)
router.register("profile", ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
