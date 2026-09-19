from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(
        'users.UserBase',
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



