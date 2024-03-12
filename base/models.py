from django.db import models
from django.utils import timezone

# Create your models here.
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # profile_photo = models.ImageField(upload_to='profile_photos/')
    language = models.CharField(max_length=50)
    status_state = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    user_status = models.CharField(choices=status_state, max_length=8, default='inactive')
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name + " " + self.surname   
    
class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.address_id + ", "+ self.city + ", " + self.district + ", " + self.ward + ", " + self.street