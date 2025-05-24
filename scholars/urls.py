from . import views
from django.urls import path
app_name = 'scholars'

urlpatterns = [
    path('', views.index, name='scholars'),
]