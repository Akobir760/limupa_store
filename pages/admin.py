from django.contrib import admin

from pages.models import ContactModel

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    list_filter = ['created_at', 'is_read']
    search_fields = ['name', 'email', 'message']
    ordering = ['-created_at']
