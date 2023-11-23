from django.shortcuts import render

# Create your views here.
def lord(request):
    return render(request,'lord.html')