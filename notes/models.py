from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.title
