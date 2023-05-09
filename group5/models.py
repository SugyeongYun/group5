from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    food_type = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    map_src = models.TextField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.user.username+" "+self.restaurant.name
    

class Question(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    message = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.message[:20]