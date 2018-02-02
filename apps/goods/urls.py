from . import views

from django.conf.urls import url
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'merchandise', views.MerchandiseViewset)
router.register(r'classification', views.Classification)
router.register(r'test', views.MerchandiseViewset)

# urlpatterns = [
#     url(r"^merchandise$", views.Merchandise.as_view()),
# ]

urlpatterns = router.urls
