from . import views

from django.conf.urls import url

from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register("person", views.PersonViewSet, base_name="person")

# urlpatterns = [
#     url(r"^$", views.Index.as_view()),
#     url(r"^test-1$", views.Test_1.as_view()),
#     url(r"^test-2$", views.Test_2.as_view()),
# ]

urlpatterns = router.urls