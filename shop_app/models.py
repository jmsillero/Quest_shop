from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Modelo categoria....
from shop_app.utils.countries import COUNTRIES


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category', null=True)


    def __str__(self):
        return self.name
# Modelo categoria....



#Modelo productos en promocion
class Promotion(models.Model):
    image = models.ForeignKey('Image', blank=True, null=True)
    product = models.ForeignKey('Product', blank=True, null=True)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
#Modelo productos en promocion



# Modelo tags...
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# Modelo tags...


#todo: cambiar serial por model
# Modelo producto...
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')
    serial = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.datetime.now())
    shop = models.ForeignKey('Shop')
    published = models.BooleanField(default=True)
    taxes = models.DecimalField(default=0.0, null=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
# Modelo producto...


#Modelo imagen....
class Image(models.Model):
    name = models.CharField(max_length=255)
    src = models.ImageField()
    product = models.ForeignKey('Product', blank=True, null=True)
    shop = models.ForeignKey('Shop', blank=True, null=True)

    def __str__(self):
        return self.name
# Modelo imagen....


#Modelo Tienda...
class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    owner = models.ForeignKey(User, related_name='owner')
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    google_plus = models.URLField()
    logo = models.ImageField(upload_to='shop/logo')
    description = models.TextField()
    country = models.CharField(choices=COUNTRIES, max_length=100, null=False, blank=False)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name
#Modelo Tienda...



class Profile(models.Model):
    CHOICE = (
        (u'owner', u'Owner'),
        (u'guest', u'Guest'),
    )

    image = models.ImageField(upload_to='profiles/', blank=True, null=True, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    type = models.CharField(choices=CHOICE, blank=False, null=False, max_length=5)
    active = models.BooleanField(default=False)
    address = models.CharField(max_length=255)


    def __str__(self):
        return self.user.username





