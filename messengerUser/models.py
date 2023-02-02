
from django.db import models
from django.contrib.auth.models import User
class MessengerUser(User):
    
    gender_choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    ]
    gender=models.CharField(max_length=1,choices=gender_choices,null=True)
    date_of_birth=models.DateField(null=True)
    
    


