from django.db import models

# Create your models here.
from django.db import models

class DiaryEntry(models.Model):
    # Заголовок записи
    title = models.CharField(max_length=100)
    # Содержимое записи
    content = models.TextField()
    # Дата и время создания записи
    created_at = models.DateTimeField(auto_now_add=True)
    # Дата и время последнего изменения записи
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Возвращаем заголовок записи
        return self.title

    def get_preview(self, length=50):
        # Возвращаем первые 'length' символов содержимого
        return self.content[:length] + '...' if len(self.content) > length else self.content
