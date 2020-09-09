from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hospital(request):
	return render(request,'hospital.html')
	
	