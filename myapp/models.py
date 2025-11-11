from django.db import models

# Create your models here.
from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
