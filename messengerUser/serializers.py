from rest_framework import serializers 
from .models import MessengerUser
class MessengerUserSerializer(serializers.ModelSerializer):
 
    

    class Meta:
        model=MessengerUser
        fields="__all__"
        # extra_kwargs={'password':{'write_only':True}}

    # def validate(self, attrs):
    #     return super().validate(attrs)
    def create(self, validated_data):
    
        return MessengerUser.objects.create(**validated_data)