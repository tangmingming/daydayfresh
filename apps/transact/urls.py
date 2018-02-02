from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter(trailing_slash=False)
router.register(r"shopingcard", views.ShoppingCardMercViewset)
router.register(r"order", views.OrderViewset)
router.register(r"ordermerc", views.OrderMercViewSet)

alipay_urlpatterns = [
  url(r"sync_return", views.AlipayAsynNoti.as_view(), name="alipaysyncreturn"),
  url(r"asyn_noti", views.AlipayAsynNoti.as_view(), name="alipayasynnoti")
]

pay_urlpatterns = [
  url(r"alipay", include(alipay_urlpatterns)),
]

urlpatterns = router.urls
