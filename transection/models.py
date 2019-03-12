from django.db import models
from category.models import Category

class Transection(models.Model):
    amount = models.FloatField(default=0)
    income = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.note