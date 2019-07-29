from django.utils import timezone

from django.db import models


# Create your models here.

class Cat(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = timezone.now()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
