from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', null=True, blank=False)

    def __str__(self):
        return self.title
