from django.db import models
from django.utils import timezone

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 100)
	authors = models.CharField(max_length = 100)
	publication_date = models.DateTimeField()
	publisher = models.CharField(max_length=100)
	summary = models.TextField()
	price = models.DecimalField(max_digits = 10, decimal_places = 3)
	link = models.URLField(max_length = 300)
	cover = models.URLField(max_length = 300)
