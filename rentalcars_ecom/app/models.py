#If we make a model we need to migrate it
from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOICE = (
    ('TY', 'Toyota'),
    ('NS', 'Nissan'),
    ('FD', 'Ford'),
    ('HN', 'Honda'),
)

STATE_CHOICES = (
    ( 'Baringo', 'Baringo'),
    ( 'Bomet', 'Bomet'),
    ( 'Bungoma', 'Bungoma'),
    ( 'Busia', 'Busia'),
    ( 'Elgeyo/Marakwet', 'Elgeyo/Marakwet'),
    ( 'Embu', 'Embu'),
    ( 'Garisa', 'Garisa'),
    ( 'Homa Bay', 'Homa Bay'),
    ( 'Isiolo', 'Isiolo'),
    ( 'Kajiado', 'Kajiado'),
    ( 'Kakamega', 'Kakamega'),
    ( 'Kericho', 'Kericho'),
    ( 'Kiambu', 'Kiambu'),
    ( 'Kirinyaga', 'Kirinyaga'),
    ( 'Kisii', 'Kisii'),
    ( 'Kisumu', 'Kisumu'),
    ( 'Kwale', 'Kwale'),
    ( 'Laikipia', 'Laikipia'),
    ( 'Lamu', 'Lamu'),
    ( 'Machakos', 'Machakos'),
    ( 'Makueni', 'Makueni'),
    ( 'Mandera', 'Mandera'),
    ( 'Meru', 'Meru'),
    ( 'Migori', 'Migori'),
    ( 'Mombasa', 'Mombasa'),
    ( 'Muranga', 'Muranga'),
    ( 'Nairobi', 'Nairobi'),
    ( 'Nakuru', 'Nakuru'),
    ( 'Nandi', 'Nandi'),
    ( 'Narok', 'Narok'),
    ( 'Nyeri', 'Nyeri'),
    ( 'Nyandarua', 'Nyandarua'),
    ( 'Siaya', 'Siaya'),
    ( 'Taita Taveta', 'Taita Taveta'),
    ( 'Tharaka Nithi', 'Tharaka Nithi'),
    ( 'Trans Nzoia', 'Trans Nzoia'),
    ( 'Uasin Gishu', 'Uasin Gishu'),
    ( 'Vihiga', 'Vihiga'),
    ( 'Wajir', 'Wajir'),
    ( 'West Pokot', 'West Pokot'),
    
)
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=2) 
    products_image = models.ImageField(upload_to="Product")
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#Foreignkey == foreign(from the other side)
    name = models.CharField(max_length=200)
    
    town = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    county = models.CharField(choices=STATE_CHOICES, max_length=100)
    def _str_(self):
        return self.name
