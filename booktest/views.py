import os
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'booktest/index.html')

def myExp(request):
    a1 = int('abc')
    return HttpResponse('hello')

def uploadPic(request):
    return render(request, 'booktest/uploadPic.html')

def uploadHandle(request):
    pic1 = request.FILES['pic1']
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(picName,'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s"/>' % pic1.name)