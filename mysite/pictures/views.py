from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo


def index(request):
    return HttpResponse("Hello, world. You're at the pictures index.")

def photos(request):
    photos =  Photo.objects.all()
    return render(request, 'pictures/photos.html', {'photos':photos})
