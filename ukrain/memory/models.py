from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Review(models.Model):
    country = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    point = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.country