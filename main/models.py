from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField(max_length=256)
    def __str__(self):
        return self.content