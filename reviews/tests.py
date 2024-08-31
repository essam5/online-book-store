from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Book
from reviews.models import Review
from django.utils import timezone

User = get_user_model()


# Create your tests here.
class ReviewTests(APITestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.force_authenticate(user=self.user)

        # Create a test book
        self.book = Book.objects.create(
            title="Book 1",
            author="Author 1",
            description="Description 1",
            available=True,
            publication_date=timezone.now(),
            isbn="test",
        )

    def test_create_review(self):
        url = reverse("review-create", args=[self.book.id])
        data = {"rating": 4, "comment": "Great book!"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.get().rating, 4)

    def test_list_reviews(self):
        # Create multiple reviews
        Review.objects.create(
            book=self.book, user=self.user, rating=4, comment="Great!"
        )
        Review.objects.create(
            book=self.book, user=self.user, rating=5, comment="Excellent!"
        )

        url = reverse("book-review-list", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["reviews"]), 2)
        self.assertEqual(
            response.data["average_rating"], 4.5
        )  # Check the average rating
