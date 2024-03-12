from rest_framework import serializers
from base.models import User, UserAddress
        
class User_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User #takes a specific table from DB
        fields = ['user_id', 'first_name', 'surname', 'email', 'password', 'language', 'user_status'] #choose which fields to serialize
        
class UserAddress_serializer(serializers.HyperlinkedModelSerializer):
    user_id = User_serializer()
    class Meta:
        model = UserAddress #takes a specific table from DB
        fields = ['address_id', 'city', 'district', 'ward', 'street', 'user_id'] #choose which fields to serialize