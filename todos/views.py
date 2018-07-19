from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id = id)
    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text )
        todo.save()
        return redirect('/')
    else:
        return render(request, 'add.html')

def delete(request, id):
    if(request.method == 'POST'):
        todo = Todo.objects.get(id = id).delete()
        temp_todo = Todo.objects.all()
        context = {
            'todo': todo,
            'temp_todo': temp_todo
        }
        return redirect('/')
    else:
        return render(request, 'details.html')