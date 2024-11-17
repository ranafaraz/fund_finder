from django.db import models

class Grant(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Run migrations to create the table:
# docker exec -it fund_finder_backend python manage.py makemigrations grants
# docker exec -it fund_finder_backend python manage.py migrate
