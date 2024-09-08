from django.http import HttpResponse;
from django.shortcuts import render 
def home(request):
    # return HttpResponse("Hello,world you are at chaiaurDjango Home page ");
    return render(request, 'index.html')
    
def about(request):
    return HttpResponse("Hello,world you are at chaiaurDjango about page ")
    
def contact(request):
    return HttpResponse("Hello,world you are at chaiaurDjango contact page ")
    

    
