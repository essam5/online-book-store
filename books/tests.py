from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Book
from django.utils import timezone

User = get_user_model()


class BookTests(APITestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.force_authenticate(user=self.user)

        # Create test books
        self.book1 = Book.objects.create(
            title="Book 1",
            author="Author 1",
            description="Description 1",
            available=True,
            publication_date=timezone.now(),
            isbn="testfirst",
        )
        self.book2 = Book.objects.create(
            title="Book 2",
            author="Author 2",
            description="Description 2",
            available=False,
            publication_date=timezone.now(),
            isbn="testsecond",
        )

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only book1 is available
        self.assertEqual(response.data[0]["title"], "Book 1")

    def test_book_detail(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book 1")
