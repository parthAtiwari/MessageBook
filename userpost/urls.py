from rest_framework.routers import DefaultRouter
from django.urls import path
from userpost import views
from rest_framework.authtoken.views import obtain_auth_token 


router=DefaultRouter()
router.register('/posts',views.PostViewSet)
router.register('/postlikes',views.PostLikesViewSet)



urlpatterns =[
    path('/like',views.like,name='like'),
    path('/home',views.home,name='home'),
    path('/createpost',views.createpost,name='createpost'),
]
    

urlpatterns+=router.urls