from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render

CHARITY_CHOICES = [
    ('healthcare', 'Healthcare'),
    ('education', 'Education'),
]
# Create your models here.
class Update(models.Model):
    donation_amount = models.CharField(max_length = 255, default='0')
    charity_name = models.CharField(max_length = 255, default='charityname')
   
    def __str__(self):
        return self.donation_amount + ' | ' + self.charity_name
    
    def get_absolute_url(self):
        return ''