from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task , CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import CustomUserCreationForm  # import the custom form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # use the custom form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')  # Redirect after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'task_manager/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description, assigned_to=request.user)
        return redirect('task_list')
    return render(request, 'task_manager/task_create.html')

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.status = request.POST['status']
        task.save()
        return redirect('task_list')
    return render(request, 'task_manager/task_update.html', {'task': task})


def role_required(role):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if request.user.role == role:
                return func(request, *args, **kwargs)
            else:
                return redirect('not_allowed')  # Redirect if role is not allowed
        return wrap
    return decorator

@login_required
@role_required('admin')
def admin_dashboard(request):
    # Admin-specific logic
    pass



@login_required
@role_required('manager')
def assign_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        assigned_to = request.POST['assigned_to']
        user = CustomUser.objects.get(id=assigned_to)
        task.assigned_to = user
        task.save()
        return redirect('task_list')
    team_members = CustomUser.objects.filter(role='member')
    return render(request, 'task_manager/assign_task.html', {'task': task, 'team_members': team_members})


@api_view(['GET'])
def api_task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('task_list')  # Redirect to task list page after login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
