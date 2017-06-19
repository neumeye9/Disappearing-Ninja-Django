from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'disappearingninja_app/index.html')

def ninja(request):
    context = {
        'ninja_name': 'all'
    }
    return render(request, 'disappearingninja_app/ninja.html', context)

def color(request, color):
    context = {
        "ninja_name" : color,
    }
    return render(request, 'disappearingninja_app/ninja.html', context)