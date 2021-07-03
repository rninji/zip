from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

def curation(request):
    return render(request,'curator_page.html')