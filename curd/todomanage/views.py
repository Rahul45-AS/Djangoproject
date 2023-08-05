from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Todo.objects.create(user=request.user, title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo_create.html')

@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_update.html', {'todo': todo})

@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_delete.html', {'todo': todo})