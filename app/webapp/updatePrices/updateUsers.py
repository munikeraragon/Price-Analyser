from django.contrib.auth.models import User
from collections import deque
import time

from userApp.webScrape import *

def main():
    # numeber of users
    userNum = User.objects.count()
    userQueue = deque(User.objects.exclude(username="MunikerSuperUser")
    # starting sleep time is 10 minutes
    sleepTime = 600
    while(True):
        time.sleep(sleepTime)
        currentUserNum = User.objects.all()
        if(userNum < currentUserNum):
            sleepTime -= (currentUserNum-userNum)*20
            userQueue = deque(User.objects.exclude(username="MunikerSuperUser")
        for user in userQueue:
            update(user)

def update(user):
    # update each item from user    
main()

