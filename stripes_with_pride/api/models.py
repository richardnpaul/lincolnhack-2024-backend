from uuid import uuid4
from django.db import models

# Create your models here.
class Score(models.Model):
    assessment = models.CharField(max_length=100, editable=False)
    score = models.IntegerField(editable=False)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
