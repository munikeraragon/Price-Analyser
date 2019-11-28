from django.contrib.auth.models import User
from collections import deque
import time

def main():
    userNum = User.objects.count()
    userQueue = deque(User.objects.exclude(username="MunikerSuperUser")
    # starting sleep time is 10 minutes
    sleepTime = 600
    while(True):
        time.sleep(600)
        currentUserNum = User.objects.all()
        if(userNum < currentUserNum):
            sleepTime -= (currentUserNum-userNum)*10
            userQueue = deque(User.objects.exclude(username="MunikerSuperUser")
        for user in userQueue:
            update(user)

def update(user):
    # update each item from user    
main()

