from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length = 80)
    code = models.CharField(max_length = 2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries" # if do not set this option, the admin page will show this data with the name of countrys, which is automatically created by Django.

class Address(models.Model):
    street = models.CharField(max_length = 80)
    postal_code = models.CharField(max_length = 5)
    city = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    address = models.OneToOneField(Address, on_delete = models.CASCADE, null = True) # Unlike foreign key, this is one-to-one so this would be not a 'set' -> no need to set related_name arg
    # book_set = ... <- this property is automatically added
    # That means we can type jkr = Author.obejcts.get(first_name = "J.K."), then jkr.book_set.all()


    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    # search on google for this keywords; django model field reference
    title = models.CharField(max_length = 50) 
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True, related_name = "books") # special field means a pointer / related_name argument enables cross queries.
    is_bestselling = models.BooleanField(default = False)
    slug = models.SlugField(default = "", blank = True,
    editable = True, null = False, db_index = True) # editable = False <- this means that this field cannot be editted at all in administration page
    published_countries = models.ManyToManyField(Country, null = False) # we didn't set related name -> when call inverse query, type like this; ger.book_set.all(), when ger is Country() object, instead of ger.books.all()

    id = models.AutoField # don't have to set this cuz this is automatically runned whithin Django database class definition
    
    def get_absolute_url(self):
        return reverse("book-detail", args = [self.slug]) # same to the url tag in DTL

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super().save(*args, **kwargs)

    def __str__(self): # whenever a book is output to the console
        return f"({self.title}) ({self.rating})"