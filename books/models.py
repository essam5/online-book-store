from django.db import models
from django.db.models import Avg


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_average_rating(self):
        average = self.reviews.aggregate(Avg("rating"))["rating__avg"]
        return round(average, 2) if average is not None else 0
