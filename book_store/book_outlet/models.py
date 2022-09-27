from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    # search on google for this keywords; django model field reference
    title = models.CharField(max_length = 50) 
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null = True, max_length = 100) # consider blank = True instead of null = True
    is_bestselling = models.BooleanField(default = False)

    id = models.AutoField # don't have to set this cuz this is automatically runned whithin Django database class definition
    
    def __str__(self): # whenever a book is output to the console
        return f"({self.title}) ({self.rating})"