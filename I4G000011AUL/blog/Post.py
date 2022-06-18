from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, time

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text= models.TextField(max_length=1000)
    Author= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date= models.DateTimeField()
    Published_date= models.DateTimeField()

    def __str__(self) -> str:
        return self.name