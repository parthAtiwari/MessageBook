from rest_framework import serializers 
from .models import UserPost,PostLikes
from messengerUser.serializers import MessengerUserSerializer
from messengerUser.serializers import MessengerUserSerializer


class PostSerializer(serializers.ModelSerializer):

    PostUser=MessengerUserSerializer()
    class Meta:

        model=UserPost
        fields="__all__"
        
    def create(self, validated_data):
    
        return UserPost.objects.create(**validated_data)

class PostLikesSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=PostLikes
        fields="__all__"
    def create(self, validated_data):
    
        return PostLikes.objects.create(**validated_data)
