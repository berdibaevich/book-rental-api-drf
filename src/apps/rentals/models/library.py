from django.db import models
from .base import BaseModel



class Library(BaseModel):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(
        'accounts.UserBase',
        on_delete=models.CASCADE,
        related_name='libraries'
    )

    class Meta:
        db_table = 'library'
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


    def __str__(self):
        return self.name