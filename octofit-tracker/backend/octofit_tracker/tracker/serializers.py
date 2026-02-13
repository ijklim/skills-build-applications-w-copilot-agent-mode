from rest_framework import serializers
from .models import UserProfile, Team, Activity, Workout, LeaderboardEntry


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = '__all__'
