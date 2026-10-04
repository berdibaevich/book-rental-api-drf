from django.db import models
from .base import BaseModel



class Store(BaseModel):
    library = models.ForeignKey(
        'rentals.Library',
        on_delete=models.CASCADE,
        related_name='stores'
    )


    class Meta:
        db_table = 'Store'
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return str(self.id)