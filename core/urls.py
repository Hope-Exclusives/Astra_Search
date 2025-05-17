from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search'),
    path('web_portfolio/', views.web_portfolio, name='web_portfolio'),
]
