from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        extra_kwargs={"password":{"write_only":True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=["id","title","content","created_at","author"]
        extra_kwargs={"author":{"read_only":True}}
    
    def create(self,validated_data):
        user=self.context['user']
        note=Note.objects.create(author=user,**validated_data)
        return note
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name","status"]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=["id","name","status"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","created_at","category","brand","description"]

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=["id","count","product","user"]