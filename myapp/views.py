from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Note

# Create your views here.

class createUserview(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteListarrayCreate(APIView):
        serializer_class=NoteSerializer
        permission_classes=[IsAuthenticated]
        
        def post(self,request):
            data=request.data
            user=request.user
            if isinstance(data,list):
                serializer=self.serializer_class(data=data,context={'user':user},many=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status":1,"message":"success","data":serializer.data},status=status.HTTP_201_CREATED)
                else:
                    return Response({"status":0,"data":serializer.errors})
            else:
                return Response({"status":0,"message":"Provided data is not an array"})
        
        def get(self,request):
            user=self.request.user
            Type=request.data['type']
            if Type=="all":
              data=Note.objects.filter(author=user)
              serializer=self.serializer_class(data,many=True)
            else:
                userId=request.data['noteid']
                data=Note.objects.filter(author=user,id=userId)
                serializer=self.serializer_class(data,many=True)
            return Response({"data":serializer.data,"message":"success","status":1},status=status.HTTP_200_OK)
            # return Response({"data":serializer.errors,"message":"faliled","status":0},status=status.HTTP_400_BAD_REQUEST)



class NoteDelete(generics.DestroyAPIView):
    serializer_class=NoteSerializer
    queryset=Note.objects.all()
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return Note.objects.filter(author=user)
    
class Createcategory(APIView):
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success","data":serializer.data,"status":1},status=status.HTTP_201_CREATED)
        else :
            return Response({"message":"failed","data":serializer.errors,"status":0},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        data=Category.objects.all()
        serializer=self.serializer_class(data,many=True)
        return Response({"message":"success","data":serializer.data,"status":1},status=status.HTTP_200_OK)

class CreateBrand(APIView):
    serializer_class=BrandSerializer
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success","data":serializer.data,"status":1},status=status.HTTP_201_CREATED)
        else :
            return Response({"message":"failed","data":serializer.errors,"status":0},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        data=Brand.objects.all()
        serializer=self.serializer_class(data,many=True)
        return Response({"message":"success","data":serializer.data,"status":1},status=status.HTTP_200_OK)

class CreateProduct(APIView):
    serializer_class=ProductSerializer
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=self.serializer_class(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success","data":serializer.data,"status":1},status=status.HTTP_200_OK)
        else:
            return Response({"message":"failed","data":serializer.errors,"status":0},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        Type=request.data['type']
        if Type=="all":
            data=Product.objects.all()
            serializer=self.serializer_class(data,many=True)
            return Response({"message":"success","data":serializer.data,"status":1},status=status.HTTP_200_OK)
        else:
            product_id=request.data["product_id"]
            data=Product.objects.filter(id=product_id)
            serializer=self.serializer_class(data,many=True)
            return Response({"message":"success","data":serializer.data,"status":True},status=status.HTTP_200_OK)
    
    def delete(self,request):
        product_id=request.data['product_id']
        if product_id:
            Product.objects.get(id=product_id).delete()
            return Response({"message":"Delete product Successfully","status":1})
        else:
            return Response({"message":"Delete product failed","status":0})
    
class Addtocart(APIView):
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"Successfully added to cart","status":1})
        else:
            return Response({"data":serializer.errors,"message":"Failed to add product to cart","status":0})
    
    def put(self,request):
        cartId=request.data.get("cartId")
 
        try:
            cart=Cart.objects.get(id=cartId)
        except Cart.DoesNotExist:
            return Response({"message":"Cart does not exist","status":0})
        serializer=self.serializer_class(cart,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"Successfully added to cart","status":1})
        else:
            return Response({"data":serializer.errors,"message":"Failed to add product to cart","status":0})
        
    def delete(self,request):
        cartId=request.data.get("cartId")
        try :
            Cart.objects.get(id=cartId).delete()
            return Response({"message":"Cart deleted successfully","status":1})
        except Cart.DoesNotExist:
            return Response({"message":"Cart does not exist","status":0})

