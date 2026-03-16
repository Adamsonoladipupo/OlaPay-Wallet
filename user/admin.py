from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "first_name", "last_name", "email", "is_staff", "is_active"),
            },
        ),
    )

    def has_delete_permission(self, request, obj = None):
        if obj and obj.is_superuser:
            return False
        return super().has_delete_permission(request, obj)