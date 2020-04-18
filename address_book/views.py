from django.shortcuts import render, redirect

# Create your views here.
# The Functions for your actuall pages

# Home Page
def home(request):
	return render(request, 'home.html', {})
	

# Add Address Page
def add_address(request):
	return render(request, 'add_address.html', {})
