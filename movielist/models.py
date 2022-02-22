from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    poster_image = models.CharField(max_length=80)
    complete_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Title: {self.title}"