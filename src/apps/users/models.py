from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserBaseManager(BaseUserManager):
    """Custom Manager"""
    def create_superuser(self, username, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("role", Role.ADMIN)
        
        user = self.model(
            username = username,
            **other_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


class Role(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    OWNER = 'OWNER', 'Owner'
    STAFF = 'STAFF', 'Staff'
    CUSTOMER = 'CUSTOMER', 'Customer'



class UserBase(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)

    is_active = models.BooleanField(_("is_active"), default=False)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    is_superuser = models.BooleanField(_("is_superuser"), default=False)

    objects = UserBaseManager()
    USERNAME_FIELD = 'username'
    

    class Meta:
        db_table = "user"
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
