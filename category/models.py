from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    cat_type = models.IntegerField()

    def __str__(self):
        return self.name