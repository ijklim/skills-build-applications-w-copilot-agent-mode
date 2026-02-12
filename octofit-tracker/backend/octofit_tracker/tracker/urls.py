from django.urls import path, include
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import (
    ActivityViewSet,
    UserProfileViewSet,
    TeamViewSet,
    WorkoutViewSet,
    LeaderboardEntryViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardEntryViewSet)


@api_view(['GET'])
def api_root(request):
    return Response({'api': request.build_absolute_uri('')})


urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
