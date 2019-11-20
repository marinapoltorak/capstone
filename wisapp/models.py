from django.db import models
from django.contrib.auth.models import User

class Scientist(models.Model):
    sci_image = models.ImageField(upload_to='images/')
    sci_name = models.CharField(max_length=200)
    sci_bio = models.TextField()
    sci_big_stuff = models.TextField()
    sci_field = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scientist')
    sci_link = models.CharField(max_length=500)

    def __str__(self):
        return self.sci_name
