from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from .models import Service

# Create your views here.

def service_list(request):
    services = Service.objects.all()

    return render(request,'services/services.html',{'services':services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)

    return render(request,template_name='services/service_detail.html',context={'service':service})
