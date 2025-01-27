from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    pubdate = models.DateField()
    
    def __str__(self):
        return self.title
    