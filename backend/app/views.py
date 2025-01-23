from django.shortcuts import render
from diary.models import DiaryEntry
from diary.tasks import process_entry

def some_view(request):
    entry = DiaryEntry.objects.create(title="Some Title", content="Some Content")  
    process_entry.delay(entry.id)
    return render(request, 'template_name.html', {'entry': entry})

from rest_framework import generics
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer