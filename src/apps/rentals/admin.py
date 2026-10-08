from django.contrib import admin
from src.utils.choices import Role

from .models import (
    Library, 
    Store,
    Category,
    Book
)

admin.site.register(Category)
admin.site.register(Book)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        user = obj.owner

        if user.role != Role.OWNER:
            user.role = Role.OWNER
            user.save(update_fields=['role'])

        return super().save_model(request, obj, form, change)


admin.site.register(Store)