from django.shortcuts import render, redirect , get_object_or_404
from core.models import Task
from core.form import TaskForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request. POST['desc']
        data = Task(title = title, desc = desc)
        data.save()
        context = {
            'success':True
        }
        return render(request,'home.html',context = context)
    return render(request,'home.html')

def task(request):
    all_data = Task.objects.all()
    context = {
        'data':all_data
    }
    return render(request, 'task.html', context = context)

def delete(request,todo_id):
    if request.method == 'POST':
        Task.objects.get(id = todo_id).delete()
        return redirect('home')

def update(request, todo_id):
    data = get_object_or_404(Task,id = todo_id)
    context = {
        "data":data
    }
    
    form = TaskForm(request.POST or None, instance = data)
    print(form)
    if form.is_valid():
        
        form.save()
        return redirect("task")
    
    return render (request, "update.html", context = context)

