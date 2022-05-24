from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
    """
    fieldsets = (
        (None, {'fields': ('username', 'password') }),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Redes sociales', {'fields': ('linkedin',)})
    )
    """