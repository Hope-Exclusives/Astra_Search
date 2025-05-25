from . import views
from django.urls import path,include
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('job_details/', views.job_details, name='job_details'),
    path('terms/', views.terms, name='terms'),
    path('profile/', views.profile, name='profile'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),

    # tech section
    path('languages/', views.languages, name='languages'),
]