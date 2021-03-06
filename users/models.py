from django.db import models
from django.contrib import admin

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=500)

class ContactAdmin (admin.ModelAdmin):
    list_display = ('name','email','message')
    # list_filter = ('name',)
    # search_fields = ('name',)
