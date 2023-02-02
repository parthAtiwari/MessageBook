from django.db import models
from django.contrib.auth.models import User
from messengerUser.models import MessengerUser
# Create your models here.
class UserPost(models.Model):
    message=models.CharField(max_length=2000,blank=False)
    PostUser=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    
class PostLikes(models.Model):
    postid=models.IntegerField()
    username=models.CharField(max_length=255)

    class Meta:
        
        unique_together = ('postid','username',)
