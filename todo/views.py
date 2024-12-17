from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm, LoginForm, TodoForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .models import CustomUser, Todo




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()   

    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile', user_id=user.id)
    else:
        form = LoginForm()
    return render(request, 'main/index.html', {'form': form})


def profile_view(request, user_id):
   user = get_object_or_404(CustomUser, id=user_id)
   todoes = Todo.objects.filter(user=user)
   return render(request, 'main/profile.html', {'user': user, 'todoes':  todoes })


def to_do(request):
   
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('profile', user_id=request.user.id)
    else:
        form = TodoForm()
    return render(request, 'main/todo.html', {'form': form})


def change_status(request , todo_id):
    todo = get_object_or_404(Todo, id=todo_id) # берм нашу заметку 
    todo.completed = not todo.completed # Меняем стутус здачи либо на завершеный либо нет 
    todo.save() # сохраняем 
    return redirect('profile', user_id=request.user.id)


def delete_todo(request , todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('profile', user_id=request.user.id)


def edit_todo(request , todo_id,):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('profile', user_id=request.user.id)
    else:
        form = TodoForm(instance=todo)

    return render(request, 'main/edit_todo.html', {'form': form})