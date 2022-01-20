from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import ToDo


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/logout/')


def insert(request: HttpRequest):
    todo = ToDo(content=request.POST['content'])
    todo.save()
    return redirect('/')


@login_required
def delete(request, todo_id):
    task_to_delete = ToDo.objects.get(id=todo_id)
    task_to_delete.delete()
    return redirect('/')


@login_required
def list_items(request):
    context = {'todo_list': ToDo.objects.all()}
    return render(request, 'todos/todo.html', context)
