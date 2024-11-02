from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notes")

    def __str__(self):
        return self.title 

class Category(models.Model):
    STATUS_CHOICES=[('Active','Active'),
                    ('Inactive','Inactive')]
    name=models.CharField(max_length=30)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')

    def __str__(self):
        return self.name 

class Brand(models.Model):
    STATUS_CHOICES=[('Active','Active'),
    ('Inactive','Inactive')]
    name=models.CharField(max_length=30)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Active')
    
    def __str__(self):
        return self.name 

class Product(models.Model):
    name=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    description=models.CharField(max_length=200,blank=True,null=True)


    def __str__(self):
        return self.name 
    
class Cart(models.Model):
    count=models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name 