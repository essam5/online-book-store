from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ReviewSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from books.models import Book
from .models import Review
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.db.models import Avg


class ReviewPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = "page_size"
    max_page_size = 100


# Submit a Review
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        book = get_object_or_404(Book, id=book_id, available=True)
        serializer.save(user=self.request.user, book=book)


# List Reviews for a Book
class BookReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = ReviewPagination

    def get_queryset(self):
        book_id = self.kwargs["book_id"]
        return Review.objects.filter(book__id=book_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response_data = self.get_paginated_response(serializer.data).data
        else:
            serializer = self.get_serializer(queryset, many=True)
            response_data = serializer.data

        # Calculate the average rating
        average_rating = queryset.aggregate(Avg("rating"))["rating__avg"]
        response_data = {
            "average_rating": round(average_rating, 2)
            if average_rating is not None
            else 0,
            "reviews": response_data,  # Include the paginated review data
        }

        return Response(response_data)
