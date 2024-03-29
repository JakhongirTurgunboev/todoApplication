from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import NameForm
from .models import Task
# Create your views here.


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


@login_required(login_url='/users/register')
def taskView(request):
    user = request.user
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print('Form validation successful')
        else:
            print('Form validation failed')
        items = request.POST.dict()
        if items.get('title') is not None and items.get('text') is not None:
            task = Task(title=items["title"], task_text=items["text"], user=user)
            task.save()
        else:
            if items.get('search') is not None:
                tasks = Task.objects.filter(Q(user=user.id,
                                            title__contains=items["search"]) |
                                            Q(user=user.id,
                                              task_text__contains=items["search"])
                                            )
                return render(request, "task/tasks.html", context={"tasks": tasks})
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
    form = NameForm()
    tasks = Task.objects.filter(user=user.id)
    return render(request, "task/tasks.html", context={"tasks": tasks, 'form': form})
