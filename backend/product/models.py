from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    PRICING_TYPES = [
        ('fixed', 'Fixed'),
        ('bidding', 'Bidding'),
        ('hourly', 'Per Hour'),
    ]
    LISTING_TYPES = [
        ('tangible', 'Physcial Products'),
        ('service', 'Services'),
    ]
    VISIBILITY_MODES = [
        ('private', 'Own University'),
        ('public', 'All registered students across participating institutions.'),
    ]
    name = models.CharField(max_length=100)
    pricing_type = models.CharField(max_length=10, choices=PRICING_TYPES)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPES)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_MODES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-amount'] 