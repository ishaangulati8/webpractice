from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import toDo

from .forms import TodoForm


# Create your views here.
def index(request):
    todo_list = toDo.objects.order_by('id')
    form = TodoForm()
    context = {'todo_list': todo_list, 'form': form}

    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    print(request.POST['text'])
    if form.is_valid():
        new_todo = toDo(text=request.POST['text'])
        new_todo.save()
    return redirect('index')


def completeTodo(request, todo_id):
    todo = toDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    toDo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    toDo.objects.all().delete()
    return redirect('index')
