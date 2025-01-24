# urls.py
from django.urls import path

from .views import DiaryEntryDetailView, DiaryEntryListCreateView

urlpatterns = [
#     path('api/register/', RegisterView.as_view(), name='register'),
#     path('api/login/', LoginView.as_view(), name='login'),
    path('entries/', DiaryEntryListCreateView.as_view(), name='diary-entry-list-create'),
    path('entries/<int:pk>/', DiaryEntryDetailView.as_view(), name='diary-entry-detail'),
]