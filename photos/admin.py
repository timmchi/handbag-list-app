from django.contrib import admin

# Register your models here.

from .models import Handbag, Category

admin.site.register(Handbag)
admin.site.register(Category)