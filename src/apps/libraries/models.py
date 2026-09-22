from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(
        'accounts.UserBase',
        on_delete=models.CASCADE,
        related_name='libraries'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'library'
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


    def __str__(self):
        return self.name




class Store(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='stores'
    )


    class Meta:
        db_table = 'Store'
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return str(self.id)
