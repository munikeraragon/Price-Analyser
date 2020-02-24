from django.db import models
from django.contrib.auth.models import User

''' Entity representation of an item '''

class Item(models.Model):
    # create many to one relationship (User -> many Items)
    currentUser = models.ForeignKey(User, on_delete=models.PROTECT)
    itemName = models.CharField(max_length=50)
    itemURL =  models.CharField(max_length=500)
    itemPrice = models.CharField(max_length=20)
    store = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.currentUser.username + "_" + str(self.itemName)