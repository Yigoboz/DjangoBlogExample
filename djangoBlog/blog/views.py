from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def post_list(request):
    posts = Blog.objects.all()

    return render(request,'blog/post_list.html',{'posts':posts})

def post_details(request, slug):
    post_detail = get_object_or_404(Blog, slug=slug)

    return render(request,template_name='blog/post_detail.html',context={'post':post_detail})
