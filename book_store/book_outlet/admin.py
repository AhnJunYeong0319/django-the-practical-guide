from django.contrib import admin

# Register your models here.
from .models import Book, Author, Address, Country

class BookAdmin(admin.ModelAdmin): # allows us to set various options that will be reflected in admin page.
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug" : ("title",)} # somewhat redundant to save() in models.py
    list_filter = ("author", "rating", )
    list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)