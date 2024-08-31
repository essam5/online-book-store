from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Display username in reviews
    book = serializers.PrimaryKeyRelatedField(read_only=True)  # Display book ID

    class Meta:
        model = Review
        fields = ["id", "book", "user", "rating", "comment", "created_at"]

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be an integer between 1 and 5."
            )
        return value
