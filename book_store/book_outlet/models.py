from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)



class Book(models.Model):
    # search on google for this keywords; django model field reference
    title = models.CharField(max_length = 50) 
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True) # special field / means a pointer
    is_bestselling = models.BooleanField(default = False)
    slug = models.SlugField(default = "", blank = True,
    editable = True, null = False, db_index = True) # editable = False <- this means that this field cannot be editted at all in administration page

    id = models.AutoField # don't have to set this cuz this is automatically runned whithin Django database class definition
    
    def get_absolute_url(self):
        return reverse("book-detail", args = [self.slug]) # same to the url tag in DTL

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super().save(*args, **kwargs)

    def __str__(self): # whenever a book is output to the console
        return f"({self.title}) ({self.rating})"