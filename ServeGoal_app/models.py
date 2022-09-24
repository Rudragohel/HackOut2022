from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(default="", max_length=254)
    password = models.CharField(default="", max_length=70)

    def __str__(self):
        return self.name
