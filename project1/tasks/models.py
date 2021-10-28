from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class JournalEntry(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 Description = models.CharField(max_length=1000, default='task')
 Category = models.CharField(max_length=128)
 Completed = models.CharField(max_length=65536, default='No')
