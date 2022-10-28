from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Place, Person


def demo(request):

    obj = Place.objects.all()
    obj_two = Person.objects.all()
    return render(request,'index.html',{'result':obj,'person':obj_two})

def about(request):

    return render(request,'about.html')