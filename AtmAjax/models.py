from django.db import models
from django.contrib.auth.models import User
import os
import random
import string

# User(username=u_name, first_name=full_name, email=email, password=made_password)

def randomStringGenerator():
    name = "I"
    name = name + str(random.randint(100, 999))
    letters = string.ascii_uppercase
    name = name + ''.join(random.choice(letters) for i in range(2))
    name = name + str(random.randint(10, 99))
    name = name + ''.join(random.choice(letters) for i in range(2))
    name = name + str(random.randint(100, 999))
    name = name + "."
    return name


def upload_location(instance, filename):
    extension = filename.split(".")[1]
    changed_file_name = randomStringGenerator()
    return "%s/%s.%s" % ("userimg", changed_file_name, extension)


class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    # picture = models.ImageField(upload_to=upload_location, default='userimg/default.png')
    card_number = models.CharField(max_length=21,null=True,blank=True)
    current_balance = models.IntegerField(null=True)
    mobile = models.CharField(max_length=15,null=True,blank=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return 'No user found'


