from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from users.views import users_router
from base.views import router
from ninja.throttling import AnonRateThrottle , AuthRateThrottle

api = NinjaAPI(
    version="1.0.0",
    throttle=[
        AuthRateThrottle(rate="100/minute"),
        AnonRateThrottle(rate="10/minute"),
    ]
)
api.add_router('', router)
api.add_router('', users_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

