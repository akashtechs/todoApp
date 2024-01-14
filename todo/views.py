from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import ToDos, Files
import os


def home(request):
    projects = ToDos.objects.all()
    files = Files.objects.all()
    return render(request, 'index.html', context={"projects": projects, "files": files})


def add_data(request):
    if request.method == "POST":
        if request.POST.get('date') != "":
            date = request.POST.get('date')
            dev_name = request.POST.get('dev')
            pro_type = request.POST.get('pro-type')
            pro_name = request.POST.get('name')
            pro_description = request.POST.get('pro-description')

            todo = ToDos.objects.create(date=date, dev_name=dev_name, pro_type=pro_type, pro_name=pro_name,
                                        pro_description=pro_description)
            todo.save()
            for fl in request.FILES.getlist('file'):
                files = Files()
                files.pro_id = todo
                files.file = fl
                files.save()

    return redirect('/home')


def open_to_do(request, id):
    project = ToDos.objects.filter(pro_id=id).first()
    return render(request, 'update.html', context={"project": project})


def update_to_do(request, id):
    if request.method == "POST":
        project = ToDos.objects.filter(pro_id=id).first()
        project.date = request.POST.get('date')
        project.dev_name = request.POST.get('dev')
        project.pro_type = request.POST.get('pro-type')
        project.pro_name = request.POST.get('name')
        project.pro_description = request.POST.get('pro-description')
        project.save()

    return redirect('/home')


def delete_to_do(request, id):
    project = ToDos.objects.filter(pro_id=id).first()
    project.delete()
    return redirect('/home')


def download(request, path):
    file_path = os.path.join(f"{settings.MEDIA_ROOT}\documents", path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def test(request):
    return HttpResponse("Hello World")
