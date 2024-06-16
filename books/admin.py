from django.contrib import admin
from . import models


@admin.register(models.Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_display_links = ['id', 'title', 'author']
