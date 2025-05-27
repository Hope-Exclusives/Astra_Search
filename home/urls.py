from . import views
from django.urls import path,include
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('job_details/', views.job_details, name='job_details'),
    path('careers/<int:job_id>/', views.job_details, name='job_details'),
    path('terms/', views.terms, name='terms'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('gallery/', views.gallery, name='gallery'),

    # tech section
    path('languages/', views.languages, name='languages'),
    path('hosting/', views.hosting, name='hosting'),
    path('databases/', views.databases, name='databases'),
    path('version_control/', views.version, name='version'),
    path('ui_tools/', views.ui_tools, name='ui_tools'),
    path('ai_tools/', views.ai_tools, name='ai_tools'),
    path('quantum/', views.quantum, name='quantum'),

    # contact form
    path('send-email/', views.send_email_view, name='send_email'),
]