from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'main/index.html', context)

def new(request):
    return render(request, 'main/new.html')

def edit(request, id):
    context = {
        'users': User.objects.get(id=id)
    }
    return render(request, 'main/edit.html', context)

def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'main/show.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/users/new')
    if request.method == 'POST':
        u = User.objects.create(full_name=request.POST['first_name'] + request.POST['last_name'], email=request.POST['email'])
    url = '/users/' + str(u.id)
    return redirect(url)

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users')

def update(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        url = "/users/"+ str(request.POST['id']) + "/edit"
        return redirect(url)
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['id'])
        user.full_name = request.POST['first_name'] + request.POST['last_name']
        user.email = request.POST['email']
        user.save()
    url = "/users/"+ str(user.id)
    return redirect(url)
