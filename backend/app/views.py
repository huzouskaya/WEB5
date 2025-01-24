from django.shortcuts import render
from app.models import DiaryEntry
from app.tasks import process_entry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

def some_view(request):
    entry = DiaryEntry.objects.create(title="Some Title", content="Some Content")  
    process_entry.delay(entry.id)
    return render(request, 'template_name.html', {'entry': entry})

from rest_framework import generics
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)