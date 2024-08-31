from django.urls import path
from .views import (
    BookReviewListView,
    ReviewCreateView,
)

urlpatterns = [
    path(
        "books/<int:book_id>/",
        BookReviewListView.as_view(),
        name="book-review-list",
    ),
    path(
        "books/<int:book_id>/create/",
        ReviewCreateView.as_view(),
        name="review-create",
    ),
]
