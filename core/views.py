from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'pages/home.html' )



def about(request):
    return render(request, 'pages/about.html')

def generator(request):


    return render(request, 'pages/generator.html')

def detail(request, id):
    
    return render(request, 'pages/Detail.html')