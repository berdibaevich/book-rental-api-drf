from django.db import models


class Category(models.Model):
    library = models.ForeignKey(
        'libraries.Library', 
        on_delete=models.CASCADE, 
        related_name='categories'
    )
    name = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name
    


class Book(models.Model):
    library = models.ForeignKey(
        'libraries.Library', 
        on_delete=models.CASCADE, 
        related_name='books'
    )
    categories = models.ManyToManyField(Category, related_name='books')
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    pages = models.PositiveIntegerField(help_text="Number of pages in the book")
    
    rental_duration = models.PositiveSmallIntegerField(
        default=7,
        help_text="Rental days limit"
    )
    rental_rate = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        help_text="Rental price"
    )
    replacement_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Cost charged if the book is lost or damaged"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


    def __str__(self):
        return f"{self.title} - {self.id}"

