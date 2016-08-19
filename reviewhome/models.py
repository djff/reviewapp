from django.db import models

# Create your models here.

from django.db import models
from mongoengine import *

class Login(Document):
    username = StringField(max_length=20)
    password = StringField(max_length=20)

class Signup(Document):
    f_name = StringField(max_length=20)
    l_name = StringField(max_length=20)
    date_of_birth = DateTimeField()
    password = StringField(max_length=20)
    email = EmailField()
