from django.shortcuts import render
from django.http import HttpResponse
from .models import product



def index(request):
    products = product.objects.all()
    return render(request,'index.html',{'products':products})
   # return HttpResponse("<h1>Welcome Django </h1>")
def about(request):
    return HttpResponse("<h1>this is about page</h1>")

# Create your views here.
