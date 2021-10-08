from django.shortcuts import render
from afktm_backend.decoraters import check_authentication

# Create your views here.

@check_authentication
def index(request):
    
    return render(request,'index.html')


@check_authentication
def teams(request):

    return render(request,'teams.html')

