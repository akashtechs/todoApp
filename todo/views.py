from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo.models import ToDos


def home(request):
    projects = ToDos.objects.all()
    return render(request, 'index.html', context={"projects": projects})


def add_data(request):
    if request.method == "POST":
        todo = ToDos()

        if request.POST.get('date') != "":
            todo.date = request.POST.get('date')
            todo.dev_name = request.POST.get('dev')
            todo.pro_name = request.POST.get('name')
            todo.pro_discription = request.POST.get('prodiscription')
            todo.save()

    return redirect('/home')


def open_to_do(request, id):
    project = ToDos.objects.filter(id=id).first()
    return render(request, 'update.html', context={"project": project})


def update_to_do(request, id):
    if request.method == "POST":
        project = ToDos.objects.filter(id=id).first()
        project.date = request.POST.get('date')
        project.dev_name = request.POST.get('dev')
        project.pro_name = request.POST.get('name')
        project.pro_discription = request.POST.get('prodiscription')
        project.save()

    return redirect('/home')
    

def delete_to_do(request, id):
    project = ToDos.objects.filter(id=id).first()
    project.delete()
    return redirect('/home')

def test(request):
    return HttpResponse("Hello World")
