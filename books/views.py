from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = "page_size"
    max_page_size = 100


# List all Books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.filter(available=True)
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = BookPagination


# Book Details
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
