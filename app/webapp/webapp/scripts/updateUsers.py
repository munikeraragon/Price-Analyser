rom django.contrib.auth.models import User
from collections import deque
import time
from userApp.models import  Item
from userApp.webScrape import *

def run():
    # numeber of users
    userNum = User.objects.count()
    userQueue = deque(User.objects.exclude(username="MunikerSuperUser"))
    # starting sleep time is 10 minutes
    sleepTime = 600
    print("before sleep")
    while(True):
        currentUserNum = User.objects.count()
        if(userNum < currentUserNum):
            sleepTime -= (currentUserNum-userNum)*20
            userQueue = deque(User.objects.exclude(username="MunikerSuperUser"))
        for user in userQueue:
            update(user)
        time.sleep(sleepTime)
def update(user):
    print("user being updated: " + str(user))
    # update each item from user
    userItems = Item.objects.filter(currentUser=user)
    print("user items: " + str(userItems))
    for item in userItems:
        currentPrice = float(item.itemPrice[1:])
        print("current price: " + str(currentPrice))
        store = item.store
        if(store == "BestBuy"):
            newPrice = float(bestBuy(item.itemURL)[1:])
            print("new price: " + str(newPrice))
        elif(store == "Amazon"):
            newPrice = float(amazon(item.itemURL)[1:])
            print("new price: " + str(newPrice))
        elif(store == "Walmart"):
            newPrice = float(walmart(item.itemURL)[1:])
            print("new price: " + str(newPrice))
        if(currentPrice>newPrice):
            item.itemPrice = "$" + str(newPrice)
            item.save()
            # alarm user

