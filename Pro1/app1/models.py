from django.db import models

# Create your models here.

class UserModel(models.Model):
    UloadImage = models.ImageField(upload_to='media/')
