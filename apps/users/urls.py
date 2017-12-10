
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

router = SimpleRouter(trailing_slash=False)
router.register("verifycode", views.VerifyCodeViewSet, base_name="verifycode")
router.register("shopuser", views.ShopUserViewSet, base_name="shopuser")

urlpatterns = router.urls


# views.ShopUserViewSet.get_object()