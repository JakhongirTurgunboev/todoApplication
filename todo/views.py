from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def taskView(request):
    if request.method == 'POST':
        items = request.POST.dict()
        if items.get('title') is not None and items.get('text') is not None:
            task = Task(title=items["title"], task_text=items["text"])
            task.save()
        else:
            for key, val in items.items():
                try:
                    key = int(key)
                    task = Task.objects.get(id=key)
                    if val == 'on':
                        task.status = True
                        task.save()
                except ValueError:
                    pass
        return redirect('/')
    tasks = Task.objects.all()
    return render(request, "tasks.html", context={"tasks": tasks})
