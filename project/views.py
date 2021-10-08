from django.contrib import messages
from django.shortcuts import render
from afktm_backend.decoraters import check_authentication
from .models import Task, Attachment
from django.shortcuts import get_object_or_404

from .forms import CKEForm
# Create your views here.

@check_authentication
def project(request):
    return render(request,'project.html')


@check_authentication
def task(request):

    user_tasks = Task.objects.all().filter(assigned_to=request.user)  
    number_of_tasks = len(user_tasks)

    context = {
        "tasks":user_tasks,
        "number_of_tasks":number_of_tasks
    }

    return render(request,'task.html',context)

@check_authentication
def detail_task(request,id):

    
    task = get_object_or_404(Task,pk=id)
    is_super = False
    remarks_form = CKEForm(request.POST or None,instance=task)

    if(request.user.is_superuser):
        is_super = True
        

    if request.method == "POST":
            
        if(request.user.is_superuser):
            command = request.POST['command']

            if(command=="send_back"):
                task.in_review = False
            elif(command=="execute"):
                
                Task.objects.filter(id=task.id).delete()

            messages.error(request,"superuser task executed.")


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
        'is_super':is_super,
        'form':remarks_form
    }

    

    return render(request,'detail_task.html',context) 