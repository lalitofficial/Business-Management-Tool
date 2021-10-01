from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request,'index.html')



def teams(request):

    return render(request,'teams.html')

