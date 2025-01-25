# diary/views.py

from rest_framework import generics
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer

class DiaryEntryListCreateView(generics.ListCreateAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DiaryEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer
