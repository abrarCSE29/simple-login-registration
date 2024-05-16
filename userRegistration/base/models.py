from django.db import models

# Create your models here.

class user(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    user_password =models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user_name + ' Password : ' + self.user_password
class attendee(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    user_password =models.CharField(max_length=50, unique=True)