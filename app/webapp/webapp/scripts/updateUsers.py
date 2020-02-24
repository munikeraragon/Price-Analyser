''' 
    Module:
        Updates all the Users in the system.

    '''
from django.contrib.auth.models import User
from collections import deque
import time
from userApp.models import  Item
from userApp.webScrape import *


def run():
    # number of users in the system
    userNum = User.objects.count()
    userQueue = deque(User.objects.exclude(username="MunikerSuperUser"))
    # initial sleep time set to 10 minutes
    sleepTime = 600

    # continously update users
    while(True):
        currentUserNum = User.objects.count()
        if(userNum < currentUserNum):
            sleepTime -= (currentUserNum-userNum)*20
            userQueue = deque(User.objects.exclude(username="MunikerSuperUser"))
        for user in userQueue:
            update(user)
        time.sleep(sleepTime)



'''
    Update the items of an user
    
    '''
def update(user):
    userItems = Item.objects.filter(currentUser=user)
    for item in userItems:
        currentPrice = float(item.itemPrice[1:])
        store = item.store
        if(store == "BestBuy"):
            newPrice = float(bestBuy(item.itemURL)[1:])
        elif(store == "Amazon"):
            newPrice = float(amazon(item.itemURL)[1:])
        elif(store == "Walmart"):
            newPrice = float(walmart(item.itemURL)[1:])
        if(newPrice<currentPrice):
            item.itemPrice = "$" + str(newPrice)
            item.save()
        

