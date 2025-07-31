from django.shortcuts import render
from .models import  Post
# Create your views here.

def index(request):
    posts3 = Post.objects.all()
    return render(request, 'library/index.html',context={'posts':posts3})