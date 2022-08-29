from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def causes(request):
    return render(request, 'causes.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')