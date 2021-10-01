from django.shortcuts import render

# Create your views here.
def project(request):
    return render(request,'project.html')

def task(request):
    return render(request,'task.html')