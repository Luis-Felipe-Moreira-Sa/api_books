from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True) 
    release_year = models.IntegerField()
    state = models.CharField(max_length=255, blank=True, null=True)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now=False, auto_now_add=True)
