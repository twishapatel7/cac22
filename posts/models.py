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

    ENVIRONMENT = 'EV'
    EDUCATION = 'ED'
    CHILDCARE = 'CC'
    HEALTHCARE = 'HC'
    ANIMALS = 'AN'
    DOMESTICVIOLENCE = 'DV'
    HOMELESS = 'HL'
    NUTRITION = 'NU'
    MILITARYVETS = 'MV'

    CHARITY_TYPE_CHOICES = [
        (ENVIRONMENT, 'environment'),
        (EDUCATION, 'education'),
        (CHILDCARE, 'child care'),
        (HEALTHCARE, 'healthcare'),
        (ANIMALS, 'animals'),
        (DOMESTICVIOLENCE, 'domestic violence'),
        (HOMELESS, 'homeless services'),
        (NUTRITION, 'nutrition'),
        (MILITARYVETS, 'military veterans')
    ]

    charity_type = models.CharField(max_length=2, choices=CHARITY_TYPE_CHOICES,default=ENVIRONMENT,)

    def __str__(self):
        return self.title + ' | ' + str(self.charity)
    
    def get_absolute_url(self):
        return reverse('home')