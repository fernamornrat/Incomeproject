from django.db import models

class Wallet(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField()
    begin = models.FloatField()

    def __str__(self):
        return self.name