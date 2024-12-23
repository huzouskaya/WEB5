from django.urls import path
from .views import diary_entries, diary_entry_detail

urlpatterns = [
    path('diary/', diary_entries, name='diary_entries'),
    path('diary/<int:pk>/', diary_entry_detail, name='diary_entry_detail'),
]