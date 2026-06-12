from django.db import models
from apps.common.models import BaseModel


class User(BaseModel):
    username = models.CharField(max_length = 150, unique = True)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 20, blank = True, null = True)
    password = models.CharField(max_length = 128, blank = True, null = True)
    
    def __str__(self):
        return self.username
