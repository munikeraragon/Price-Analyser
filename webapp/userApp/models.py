from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    # create a many to one relationship (User -> many Items)
    currentUser = models.ForeignKey(User, on_delete=models.PROTECT)
    itemName = models.CharField(max_length=50)
    itemURL =  models.CharField(max_length=250)
    itemPrice = models.CharField(max_length=20)
    def __str__(self):
        return self.currentUser.username + "_" + str(self.itemName)