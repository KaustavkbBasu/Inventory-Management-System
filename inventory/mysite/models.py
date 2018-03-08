from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class StoreManager(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField()


    class Meta:
        ordering = ('-username',)
    def __str__(self):
        return self.username

class Inventory(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
    )

    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    MRP = models.IntegerField(blank=False)
    batchNum = models.IntegerField(blank=False)
    batchDate = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def get_absolute_url(self):
        return reverse('inventory_detail',kwargs={'pk':self.productId})
