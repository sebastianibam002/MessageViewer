from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class DateIdeas(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    priority = models.IntegerField()
    posible_duration = [('short', 'short'), ('medium', 'medium'), ('long', 'long')]
    duration = models.CharField(choices=posible_duration, default='short', max_length=6)
    check_done = models.BooleanField(default=False)
    review = models.TextField(default="")
    image = models.ImageField(upload_to="media", null=True, default="media/empty.jpg")
    date_done = models.DateField(default=None, null=True)

    def __str__(self) -> str:
        return f"Title: {self.title}"