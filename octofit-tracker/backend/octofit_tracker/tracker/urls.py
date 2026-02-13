import os
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
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        api_base = f"https://{codespace}-8000.app.github.dev/api/"
    else:
        root = request.build_absolute_uri('/')
        api_base = root.rstrip('/') + '/api/'

    return Response({
        'users': api_base + 'users/',
        'teams': api_base + 'teams/',
        'activities': api_base + 'activities/',
        'workouts': api_base + 'workouts/',
        'leaderboard': api_base + 'leaderboard/',
    })


urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
