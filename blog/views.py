from django.shortcuts import render
from .models import  Post
# Create your views here.

def index(request):
   #db에서 qurey 날린거임
    posts1111=Post.objects.all()
    return render(request, 'blog/index.html',context={'posts':posts1111})

def detail(request, pk):
    post1 = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html',context={'post':post1})