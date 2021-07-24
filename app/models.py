from django.db import models

# Create your models here.

class Password(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField()
    password = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return f" {self.username} {self.email} {self.password} "
