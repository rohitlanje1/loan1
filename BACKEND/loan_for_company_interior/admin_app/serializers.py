from rest_framework import serializers
from .models import User,Defaulter

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","dob","gender","email","address","city","state","country","pin_code","mobile","photo","signature","role",]

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)

class DefaulterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defaulter
        fields = ["id","user","default_amount","pending_since_date"]
