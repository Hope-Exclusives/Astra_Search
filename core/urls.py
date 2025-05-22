from django.urls import path
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search'),
    path('images/', views.search_images, name='images'),
    path('web_portfolio/', views.web_portfolio, name='web_portfolio'),
]
