# models.py
from django.db import models

class Reminder(models.Model):
    reminder_datetime = models.DateTimeField(null=True)
    sendingDate = models.TextField(null=True)
    sendingTime = models.TextField(null=True)
    message = models.TextField()
