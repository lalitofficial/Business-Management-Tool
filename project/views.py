from django.contrib import messages
from django.http.response import Http404
from django.shortcuts import redirect, render
from afktm_backend.decoraters import check_authentication
from .models import Task
from django.shortcuts import get_object_or_404

from .forms import CKEForm
# Create your views here.

@check_authentication
def project(request):
    return render(request,'project.html')


@check_authentication
def task(request):


    if(request.user.is_superuser):
        user_tasks = Task.objects.all().filter(assigned_by=request.user)

    elif(not request.user.is_superuser):
        user_tasks = Task.objects.all().filter(assigned_to=request.user)

    number_of_tasks = len(user_tasks)
        

    context = {
        "tasks":user_tasks,
        "number_of_tasks":number_of_tasks
    }

    return render(request,'task.html',context)


def check_malicious(request,model):
    if model.assigned_by == request.user or model.assigned_to == request.user:
        return True

    return False

@check_authentication
def detail_task(request,id):

    
    task = get_object_or_404(Task,pk=id)

    # check if user accessing the task have access to the task

    if not check_malicious(request,task):
        raise Http404('You are not allowed to access')


    
    remarks_form = CKEForm(request.POST or None,instance=task)

    
    

    if request.method == "POST":
            
        if(request.user.is_superuser):
            try:
                command = request.POST['command']
            except:
                command = None

            if(command=="send_back"):
                task.in_review = False
                task.save()
            elif(command=="execute"):
                
                task.delete()
                return redirect('task')
            else:
                messages.error(request,"select a task")


        else:
           
            if not task.in_review:
                
                remarks_form = CKEForm(request.POST,instance=task)

                if remarks_form.is_valid():
                    remarks_form.save()
                    task.set_review()

                


            else:
                messages.error(request,"task is in review")
            
           

    context = {
        "task":task,
        'is_super':request.user.is_superuser,
        'form':remarks_form
    }

    

    return render(request,'detail_task.html',context) 