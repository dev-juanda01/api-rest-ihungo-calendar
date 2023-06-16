from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, NotificationForUserViewSet  # , ActivePartnersViewSet

router = DefaultRouter()

# router.register(r'partners/actives', ActivePartnersViewSet)
router.register(r'users', UserViewSet)
router.register(r'notifications', NotificationForUserViewSet)

urlpatterns = router.urls
