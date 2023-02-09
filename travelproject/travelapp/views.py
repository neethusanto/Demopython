from django.shortcuts import render
from . models import  place,teammembers

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=teammembers.objects.all()
    return render(request, "index.html",{'result':obj,'teamresult':obj1})