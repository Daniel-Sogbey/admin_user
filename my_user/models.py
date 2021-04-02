from django.db import models

# Create your models here.
class userregisterform(models.Model):
    email1 = models.EmailField('email address' ,  blank=False)
    email2 = models.EmailField('email address' , blank=False)
    password = models.CharField('Password' , max_length=12)
    place_of_birth = models.CharField('place of living' , max_length=20 )
    current_residence = models.CharField('where you are living now' , max_length=20)
    
    
