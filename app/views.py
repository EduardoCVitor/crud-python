from django.shortcuts import render


# Create your views here.

def home(request):                      # Define a função Home que ao ser chamada
    return render(request, "index.html")

def form(request):                      # Define a função Home que ao ser chamada
    return render(request, "form.html")
