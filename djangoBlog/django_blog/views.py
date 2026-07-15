from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service
from blog.models import Blog
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):

    featured = Service.objects.filter(is_featured=True)
    latest_models = Blog.objects.all()[:3]

    return render(request,template_name='django_blog/index.html',context={'featured':featured,'latest_models':latest_models})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Hyperspace Contact Form"
        message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        recipient_list = [settings.EMAIL_HOST_USER]

        try:
            send_mail(subject, message_body, email, recipient_list)
        except Exception:
            messages.error(request,"Something Went Wrong!")
        else:
            messages.success(request,"Message Sent!")

    return HttpResponseRedirect(reverse('index') + '#three')

