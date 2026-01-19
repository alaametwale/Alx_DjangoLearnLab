from django.contrib import admin
from .models import CustomUser, Book


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser')


# ✅ REQUIRED by ALX checker (DO NOT use decorator)
admin.site.register(CustomUser, CustomUserAdmin)

# Book model registration
admin.site.register(Book)
