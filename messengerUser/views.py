from django.shortcuts import render,redirect

from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from django.db import models
from .models import MessengerUser
from messengerUser.serializers import MessengerUserSerializer
import json
from userpost.views import PostViewSet

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.decorators import permission_classes,authentication_classes
from userpost.serializers import PostSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny,IsAuthenticated
from userpost.models import UserPost
class MessengerUserViewSet(ModelViewSet):
    queryset=MessengerUser.objects.all()
    serializer_class=MessengerUserSerializer

from django.shortcuts import render

def HomePage(request):
    return render(request,'homepage.html')

# @api_view(http_method_names=['GET'])
# def homepage(request):
#     return Response({
#         'message':'welcome MessageBook user',
#     },status=200)





# @permission_classes([AllowAny])
def registerpage(request):
    return render(request,'register.html')
def loginpage(request):
    return render(request,'login.html')

# @api_view(http_method_names=['POST',"GET"])
def register_user(request):
    try:
        
        # error={"message":"Provide valid credentials"}
        # success= {'message':'user registered successfully'}
        if request.POST['password']==request.POST['confirmpassword']:
            # obj=MessengerUserSerializer(data=request.POST)
            # obj.is_valid(raise_exception=True)
            obj=MessengerUser(username=request.POST['username'],gender=request.POST['gender'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],date_of_birth=request.POST['date_of_birth'])
            obj.set_password(request.POST['password'])
            obj.save()
            return render(request,'homepage.html',{'message':'user registered successfully'})
            # if obj.is_valid():

                

            #     obj.save()
                
            
            # return Response({
            #     'message':'user registered successfully',
            #     'status':201
            # },status=201)
        else:
            
            return render(request,'homepage.html',{'error':"Invalid credentials"})
            # return Response({
            #     'message':'password do not match'
            # },status=401)
    except Exception as e:
        return render(request,'homepage.html',{'error':e.__str__})
        

# @api_view(http_method_names=["POST",'GET'])
def login_user(request):
    try:
        
        # customer_obj=Customer.objects.filter(username=request.data['username'])[0]
        user_obj= authenticate(request,username=request.POST['username'], password=request.POST['password'])
        if user_obj is not None:
            
            login(request,user_obj)
            
            
                # fname=i[1]['first_name']
                # lname=i[1]['last_name']
                # message=i[2]
                # posts.append({'name':fname+' '+lname,"msg":message})

                
               
                


            return redirect(to="/feed/home")
            
            # return Response({
            #     'message':'user logged in',
                
            # },status=200)
        else:
            
            return render(request,'homepage.html',{'error':"Invalid credentials"})
            # return Response({
            #     'message':'invalid password or user'
                
            # },status=200)
    except Exception as e:
        
        return render(request,'homepage.html',{'error':'login failed'})
        # return Response({
        #     'message':e.__str__()
        # },status=401)
@login_required()
@api_view(http_method_names=['GET'])
def logout_user(request):
    try:

        logout(request)
        return render(request,'homepage.html',{'message':'User LoggedOut Successfully'})
        # return Response({
        #     'message':'user Logged out successfully '
        # },status=200)

    except Exception as e:
        return render(request,'homepage.html',{'message':'Logout failed'})
        # return Response({
        #     'message':'Logout failed'
        # },status=403)