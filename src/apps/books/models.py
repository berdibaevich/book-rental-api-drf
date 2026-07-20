from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=255)
    categories = models.ManyToManyField(
        Category,
        related_name='books'
    )
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title

