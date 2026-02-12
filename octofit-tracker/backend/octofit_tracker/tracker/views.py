from rest_framework import viewsets
from .models import UserProfile, Team, Activity, Workout, LeaderboardEntry
from .serializers import (
    UserProfileSerializer,
    TeamSerializer,
    ActivitySerializer,
    WorkoutSerializer,
    LeaderboardEntrySerializer,
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('name')
    serializer_class = UserProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all().order_by('-timestamp')
    serializer_class = WorkoutSerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('-points')
    serializer_class = LeaderboardEntrySerializer
