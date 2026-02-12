from django.urls import path, include
from rest_framework import routers
from .views import ActivityViewSet

router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
