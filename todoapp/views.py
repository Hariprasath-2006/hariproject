from django.shortcuts import render,redirect
from .models import task
from .forms import task_form
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def task_list(request):
    tasks = task.objects.filter(user = request.user)
    return render(request,'task_list.html',{'tasks':tasks})

@login_required
def task_forms(request):
    if request.method == 'POST':
        task_obj = task_form(request.POST)
        if task_obj.is_valid():
            Task = task_obj.save(commit=False)
            Task.user = request.user
            Task.save()
            return redirect('task_list')
        
    else:
        task_obj = task_form()


    return render(request,'add_task.html',{'form':task_obj})  
@login_required
def update_task(request,pk):
    taskvar = get_object_or_404(task,pk = pk,user = request.user)
    if request.method == 'POST':
        task_obj = task_form(request.POST,instance = taskvar)
        if task_obj.is_valid():
            task_obj.save()
            return redirect('task_list')
        
    else:
        task_obj = task_form(instance=taskvar)
        
    return render(request,'add_task.html',{'form':task_obj})

def delete_task(request,pk):
    taskvar = get_object_or_404(task,pk = pk ,user = request.user)
    if request.method == 'POST':
     
        taskvar.delete()
        return redirect('task_list')
    return render(request,'delete_confirm.html',{'task':taskvar})
