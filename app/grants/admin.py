from django.contrib import admin
from .models import Grant

@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'created_at', 'updated_at')


# docker exec -it fund_finder_backend python manage.py makemigrations
# docker exec -it fund_finder_backend python manage.py migrate
# docker-compose -f docker/compose.dev.yml restart