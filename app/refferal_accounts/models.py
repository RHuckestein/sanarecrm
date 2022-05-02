from django.db import models

# Create your models here.
class RefferalAccount(models.Model):
    username = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=200, blank=False, default='')
    first_name = models.CharField(max_length=30, blank=False, default='')
    last_name = models.CharField(max_length=30, blank=False, default='')
    phone = models.CharField(max_length=10, blank=False, default='')
    email = models.CharField(max_length=10, blank=False, default='')