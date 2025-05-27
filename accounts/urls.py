from django.urls import path
from . import  views
app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.sign_up, name='signup'),
    path('sign-in/', views.sign_in, name='signin'),
    path('forgot/', views.forgot, name='forgot'),
    path('reset/', views.reset, name='reset'),
    path('soon/', views.soon, name='soon'),
    path('maintainance/', views.maintain, name='maintainance')
]