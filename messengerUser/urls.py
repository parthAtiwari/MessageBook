from rest_framework.routers import DefaultRouter
from django.urls import path
from messengerUser import views
from rest_framework.authtoken.views import obtain_auth_token 


router=DefaultRouter()
router.register('/users',views.MessengerUserViewSet)



urlpatterns = [
    path('',views.HomePage,name='homepage'),
    path('/register',views.registerpage,name='register'),
    path('/login',views.loginpage,name='login'),
    path('/postregister',views.register_user,name='register_user'),
    path('/postlogin',views.login_user,name='loginuser'),
    path('/postlogout',views.logout_user,name='logout_user'),
    
    
]
urlpatterns+=router.urls