from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Home")

def about(request):
    return HttpResponse("Hello ABOUT")

def contact(request):
    return HttpResponse("Hello CONTACT")

