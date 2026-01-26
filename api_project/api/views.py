from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListAPIView - لعرض الكتب فقط
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# ModelViewSet - CRUD كامل
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
