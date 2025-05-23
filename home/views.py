from django.shortcuts import render


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
