from django.shortcuts import render
from afktm_backend.decoraters import check_authentication
from project.models import Task

# Create your views here.

@check_authentication
def index(request):
    
    if(request.user.is_superuser):
        tasks = Task.objects.all().filter(assigned_by=request.user)[:4]

    else:
        tasks = Task.objects.all().filter(assigned_to=request.user)[:4] 

    context = {
        'tasks':tasks
    }

    return render(request,'index.html',context)


@check_authentication
def teams(request):

    return render(request,'teams.html')

