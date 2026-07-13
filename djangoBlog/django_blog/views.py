from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service

# Create your views here.

def index(request):

    featured = Service.objects.filter(is_featured=True)

    return render(request,template_name='django_blog/index.html',context={'featured':featured})