from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user + "profile"
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    photo = models.ImageField(upload_to='product_images', blank=True)
    price = models.FloatField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    TVA_AMOUNT = 19.25

    def price_ttc(self):
        return self.price + self.TVA_AMOUNT

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='category_images', blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

    
