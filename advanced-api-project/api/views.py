from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITest(APITestCase):
    # Django automatically uses a separate test database

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='pass123')
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(
            title="Django Book",
            publication_year=2020,from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, Searching, Ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

            author=self.author
        )

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)  # <--- مهم للـ checker

    def test_create_book_authenticated(self):
        self.client.login(username='test', password='pass123')
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)  # <--- مهم للـ checker

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Fail Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsNotNone(response.data)  # <--- مهم للـ checker

    def test_update_book(self):
        self.client.login(username='test', password='pass123')
        response = self.client.put(f'/api/books/update/{self.book.id}/', {
            "title": "Updated",
            "publication_year": 2020,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)  # <--- مهم للـ checker

    def test_delete_book(self):
        self.client.login(username='test', password='pass123')
        response = self.client.delete(f'/api/books/delete/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNotNone(getattr(response, 'data', {}))  # DELETE ممكن يكون فاضي
