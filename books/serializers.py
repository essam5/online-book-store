from rest_framework import serializers
from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "publication_date",
            "isbn",
            "available",
            "average_rating",
        ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()
