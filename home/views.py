from django.shortcuts import render, redirect, get_object_or_404
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from .models import Job  # import your Job model

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

# Read jobs from the database and render them

def careers(request):
    jobs = Job.objects.all()
    return render(request, 'home/careers.html', {'jobs': jobs})


def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    context = {
        'job': job,
        'responsibilities': job.responsibilities.split('\n'),
        'requirements': job.requirements.split('\n'),
        'benefits': job.benefits.split('\n'),
    }
    return render(request, 'home/job_details.html', context)



def terms(request):
    return render(request, 'home/terms.html')

def profile(request):
    return render(request, 'home/profile.html')

def blog(request):
    return render(request, 'home/blog.html')

def blog_single(request):
    return render(request, 'home/blog-single.html')



def languages(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'languages')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/languages/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/languages.html', {'page_obj': page_obj})




def hosting(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'hosting')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/hosting/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/hosting.html', {'page_obj': page_obj})



def databases(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'databases')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/databases/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/databases.html', {'page_obj': page_obj})




def version(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'version')

    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]

    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/version/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/version.html', {'page_obj': page_obj})


def ui_tools(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'ui-tools')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/ui-tools/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/ui-tools.html', {'page_obj': page_obj})



def ai_tools(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'ai-tools')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/ai-tools/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/ai-tools.html', {'page_obj': page_obj})



def quantum(request):
    image_folder = os.path.join(settings.BASE_DIR, 'home', 'static', 'assets', 'img', 'logos', 'quantum')
    
    if not os.path.exists(image_folder):
        image_files = []
    else:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
    
    # Only relative path from 'static' folder
    image_urls = [f"assets/img/logos/quantum/{img}" for img in image_files]

    paginator = Paginator(image_urls, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/tech/quantum.html', {'page_obj': page_obj})




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




def send_email_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Contact Form Message from {name}"
        full_message = f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                email,  # From email
                ['kipkoechishmaelbett@gmail.com'],  # Replace with your receiving email
                fail_silently=False,
            )
            messages.success(request, 'Your message was sent successfully!')
        except Exception as e:
            print("Error sending email:", e)
            messages.error(request, 'Something went wrong. Please try again.')

        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('/')



