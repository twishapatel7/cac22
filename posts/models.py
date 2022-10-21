from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255)
    charity = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    charity_email = models.CharField(max_length = 255, default='charityemail')
    charity_website = models.TextField(default='charitywebsite')
    donation_goal = models.CharField(max_length=255, default='10000')

    def __str__(self):
        return self.title + ' | ' + str(self.charity)
    
    def get_absolute_url(self):
        return reverse('home')