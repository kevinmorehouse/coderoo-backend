from django.urls import path
from rest_framework.routers import SimpleRouter


from .views import UserViewSet, RoomViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", RoomViewSet, basename="rooms")

urlpatterns = router.urls
