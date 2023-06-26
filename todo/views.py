from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


def taskView(request):
    if request.method == 'POST':
        items = request.POST.dict()
        print(items)
        if items.get('title') is not None and items.get('text') is not None:
            task = Task(title=items["title"], task_text=items["text"])
            task.save()
        else:
            tasks = Task.objects.all()
            for task in tasks:
                task.status = False
                task.save()
            for key, val in items.items():
                try:
                    key = int(key)
                    task = Task.objects.get(id=key)
                    if val == 'on':
                        task.status = True
                        task.save()
                except ValueError:
                    if 'delete' in key:
                        id = int(key.split('delete')[1])
                        task = Task.objects.get(id=id)
                        task.delete()
        return redirect('/')
    tasks = Task.objects.all()
    return render(request, "task/tasks.html", context={"tasks": tasks})
