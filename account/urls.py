# from django.urls import path, include
# from . import views
#
#
# urlpatterns = [
#     path("register", views.register_request, name="register"),
#     path("login", views.loginView, name="login"),
#     path("logout", views.logout_view, name="logout")
# ]


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register(r'tasks', views.TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('hello/', views.hello_world),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]