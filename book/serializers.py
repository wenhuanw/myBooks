from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
         model = Book
         fields = ('title', 'authors', 'publication_date', 'publisher', 'summary', 'price', 'link','cover')
    title = serializers.CharField(max_length = 100)
    authors = serializers.CharField(max_length = 100)
    publication_date = serializers.DateTimeField()
    publisher = serializers.CharField(max_length=100)
    summary = serializers.CharField(max_length=400)
    price = serializers.DecimalField(max_digits = 10, decimal_places = 3)
    link = serializers.URLField(max_length = 300)
    cover = serializers.URLField(max_length = 300)

    def create(self, validated_data):
         return Book.objects.create(**validated_data)


    def update(self, instance, validated_data):
         instance.title = validated_data.get('title',instance.title)
         instance.authors = validated_data.get('authors',instance.authors)  
         instance.publication_date = validated_data.get('publication_date',instance.publication_date)
         instance.publisher = validated_data.get('publisher',instance.publisher)
         instance.summary = validated_data.get('summary',instance.summary)
         instance.price = validated_data.get('price',instance.price)
         instance.link = validated_data.get('link',instance.link)
         instance.cover = validated_data.get('cover',instance.cover)
         instance.save()
         return instance

