from rest_framework import viewsets
from books.api import serializers
from books import models

class booksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.booksSerializer
    queryset = models.Books.objects.all()
