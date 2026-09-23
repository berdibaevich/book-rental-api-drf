from django.db import models


class Role(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    OWNER = 'OWNER', 'Owner'
    STAFF = 'STAFF', 'Staff'
    CUSTOMER = 'CUSTOMER', 'Customer'