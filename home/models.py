from django.db import models

# Create your models here.

"""
Stores the message that is given in the UI
with the last color of the four rgb
"""
class StateOfDevice(models.Model):
    message = models.CharField(max_length=150)
    led_one_hex = models.CharField(max_length=10)
    led_two_hex = models.CharField(max_length=10)
    led_three_hex = models.CharField(max_length=10)
    led_four_hex = models.CharField(max_length=10)