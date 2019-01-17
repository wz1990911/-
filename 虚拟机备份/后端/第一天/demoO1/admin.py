from django.contrib import admin

# Register your models here.
from demoO1.models import Book,Publisher
admin.site.register(Book)
admin.site.register(Publisher)