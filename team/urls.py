from django.urls import path, include
from .views import TeamViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('', include(router.urls)),
]