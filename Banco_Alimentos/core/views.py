from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def products(request):
    return render(request, 'core/products.html')