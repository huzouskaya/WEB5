from rest_framework import routers, serializers, viewsets
from .models import DiaryEntry

class DiarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']