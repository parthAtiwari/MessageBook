from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from . models import UserPost,PostLikes
from userpost.serializers import PostSerializer,PostLikesSerilaizer
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework.response import Response
class PostViewSet(ModelViewSet):
    
    queryset=UserPost.objects.all()
    serializer_class=PostSerializer

class PostLikesViewSet(ModelViewSet):
    
    queryset=PostLikes.objects.all()
    serializer_class=PostLikesSerilaizer


@login_required()
@api_view(http_method_names=['GET'])
def home(request):
    posts=[]
    for obj in UserPost.objects.all():
                i=list(PostSerializer(obj))
               
                postid=i[0].value
                msg=i[2].value
                name=i[1].value['first_name']+' '+i[1].value['last_name']
                likes=i[3].value
                likestatus=PostLikes.objects.filter(postid=postid,username=request.user.username)
                if likestatus:
                    posts.append({'msg':msg,'name':name,'likes':likes,'postid':postid,'likestatus':likestatus})
                else:
                    posts.append({'msg':msg,'name':name,'likes':likes,'postid':postid})
                
    posts=posts[::-1]
    return render(request,'newsfeed.html',{'posts':posts})

@api_view(http_method_names=["POST"])
def createpost(request):
    try:
        msg=request.POST['message'].strip()

        if msg!='':
            # d={'message':request.data['message'],'PostUser':request.user,'likes':0}
            # obj=PostSerializer(data=request.POST)
            
            # obj.is_valid(raise_exception=True)

            post_obj=UserPost(message=msg,PostUser=request.user)

            post_obj.save()
            return redirect(to='/feed/home')
        else:
            return redirect(to='/feed/home')
            

        # return Response({
        #         'message':'message posted successfully',
        #         'status':201
        #     },status=201)
    except Exception as e:
       
        return redirect(to='/feed/home')
        # return Response({
        #     'message':e.__str__(),
           
            
        # },status=400)

def like(request):
    status=PostLikes.objects.filter(postid=request.POST['postid'],username=request.user.username)
    
    if not status:
        PostLikes.objects.create(postid=request.POST['postid'],username=request.user.username)
        post_obj=UserPost.objects.get(id=request.POST['postid'])
        
        post_obj.likes+=1
        post_obj.save()
     
        return redirect(to='/feed/home')
    else:
        instance=PostLikes.objects.get(postid=request.POST['postid'],username=request.user.username)
        instance.delete()
        post_obj=UserPost.objects.get(id=request.POST['postid'])
        
        post_obj.likes-=1
        post_obj.save()
        return redirect(to='/feed/home')


   

    
    



