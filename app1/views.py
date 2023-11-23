from django.shortcuts import render

# Create your views here.
def flower(request):
    return render(request,'flower.html')