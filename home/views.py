from django.shortcuts import render
import os
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def careers(request):
    return render(request, 'home/careers.html')

def job_details(request):
    return render(request, 'home/job_details.html')

def terms(request):
    return render(request, 'home/terms.html')

def profile(request):
    return render(request, 'home/profile.html')

def blog(request):
    return render(request, 'home/blog.html')

def languages(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/languages.html', {'page_obj': page_obj})


def gallery(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'carousel')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/carousel/{img}" for img in image_files]

    paginator = Paginator(image_urls, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/gallery.html', {'page_obj': page_obj})


