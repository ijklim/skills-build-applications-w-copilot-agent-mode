from rest_framework import viewsets
from .models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer
