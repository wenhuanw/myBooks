from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
        title = serializers.CharField(max_length = 100)
        authors = serializers.CharField(max_length = 100)
        publication_date = serializers.DateTimeField()
        publisher = serializers.CharField(max_length=100)
        summary = serializers.TextField()
        price = serializers.DecimalField(max_digits = 10, decimal_places = 3)
        link = serializers.URLField(max_length = 300)
        cover = serializers.URLField(max_length = 300)

 def create(self, validated_data):
