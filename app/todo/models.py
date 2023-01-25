from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    description= models.TextField(default='')
    deadline = models.DateTimeField()
    isCompleted= models.BooleanField(default=False)
    