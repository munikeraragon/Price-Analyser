from django.contrib.auth.models import User

def getUser(userName):
    print(User.objects.all())
    user = User.objects.get(username=userName)
    print("Able to obtain user -> " + str(user))
