from django.shortcuts import render

# Create your views here.
def Main_Page(request):
    return render(request, 'blog/index.html', {})

def CV_Page(request):
    return render(request, 'blog/cv.html', {})