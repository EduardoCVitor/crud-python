from django.shortcuts import render
from app.forms import CarrosForm

# Create your views here.

def home(request):                      # Define a função Home que ao ser chamada
    return render(request, 'index.html')

def form(request):                      # Define a função Home que ao ser chamada
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)
 