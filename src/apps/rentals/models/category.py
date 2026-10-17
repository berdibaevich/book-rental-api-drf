from django.db import models
from .base import BaseModel


class Category(BaseModel):
    library = models.ForeignKey(
        'rentals.Library', 
        on_delete=models.CASCADE, 
        related_name='categories'
    )
    name = models.CharField(max_length=100)


    class Meta:
        db_table = "category"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        constraints = [
            models.UniqueConstraint(
                fields=['library', 'name'], name='unique_library_category_name'
            )
        ]


    def __str__(self):
        return self.name