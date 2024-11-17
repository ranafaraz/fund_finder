from django.contrib import admin
from .models import Grant

@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'created_at', 'updated_at')
