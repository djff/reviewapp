from django.db import models

# Create your models here.

from django.db import models
from mongoengine import *

class Signup(Document):
    f_name = StringField(max_length=20)
    l_name = StringField(max_length=20)

    def __str__(self):
        return '{0} {1}'.format(self.f_name, self.l_name)git s