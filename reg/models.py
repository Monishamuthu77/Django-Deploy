from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    email = models.EmailField()
    url = models.URLField()
    phone = models.BigIntegerField(unique=True)
    aadhar = models.BigIntegerField(unique=True)
    img = models.FileField()
