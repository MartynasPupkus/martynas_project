from django.contrib import admin
from . import models

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status',)

admin.site.register(models.Post, AuthorAdmin)