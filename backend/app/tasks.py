from celery import shared_task
from .models import DiaryEntry

@shared_task
def process_entry(entry_id):
    entry = DiaryEntry.objects.get(id=entry_id)