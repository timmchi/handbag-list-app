from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Handbag(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    bio = models.TextField(null=True)
    price = models.TextField(null=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    


    def __str__(self):
        return self.description