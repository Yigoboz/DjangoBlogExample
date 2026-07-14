from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service
from blog.models import Blog

# Create your views here.

def index(request):

    featured = Service.objects.filter(is_featured=True)
    latest_models = Blog.objects.all()[:3]

    return render(request,template_name='django_blog/index.html',context={'featured':featured,'latest_models':latest_models'})