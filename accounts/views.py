from django.shortcuts import render

# Create your views here.

def sign_up(request):
    return render(request, 'accounts/sign-up.html')

def sign_in(request):
    return render(request, 'accounts/sign-in.html')

def forgot(request):
    return render(request, 'accounts/forgot.html')

def reset(request):
    return render(request, 'accounts/reset.html')

def soon(request):
    return render(request, 'accounts/soon.html')

def maintain(request):
    return render(request, 'accounts/maintainance.html')