from django.shortcuts import render
from .models import *


# Create your views here.
def Main_Page(request):
    return render(request, 'blog/index.html', {})

def CV_Page(request):
    # CvFile = CV.objects.all()
    # context = {
    #     'CvFile':CvFile,
    # }
    return render(request, 'blog/cv.html', {})
