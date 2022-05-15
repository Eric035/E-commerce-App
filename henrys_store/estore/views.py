from django.shortcuts import render

# Create your views here.

def estore(request):
  return render(request, 'estore/estore.html')

def checkout(request):
  return render(request, 'estore/checkout.html')

def cart(request):
  return render(request, 'estore/cart.html')