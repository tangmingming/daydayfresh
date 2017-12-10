"""daydayfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from goods import views

from django.conf.urls import url, include

import xadmin
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

from daydayfresh.settings import MEDIA_ROOT
from django.views.static import serve

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register("mer", views.Merchandise)

from goods.urls import router as goods_router
from rest_framework.authtoken import views

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r"^media/(?P<path>.*)$", serve, {"document_root": MEDIA_ROOT}),
    url(r"^api/goods/", include(goods_router.urls)),
    # url(r"^api/", include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r"^c-test/", include("c_test.urls")),
    url(r"^user/", include("users.urls")),
    url(r"^goods/", include("goods.urls")),
    url(r"^docs", include_docs_urls(title="天天生鲜借口文档")),
]
